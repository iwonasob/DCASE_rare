'''
Run system on test files, evaluate with ROC curves
'''

import config as cfg
import os
import numpy as np
import cPickle
import multiprocessing
from tqdm import tqdm
from sklearn import  ensemble, metrics
from joblib import Parallel, delayed
from nmf import NMF, process_parallel
import csv

np.random.seed(1515)
eps = np.spacing(1)
num_cores = multiprocessing.cpu_count()

from IPython.core.debugger import Tracer

class Evaluator:
    """
    Tests and evaluates the system
    """   
    def __init__(self,lam, rank_0, rank_1):
        self.iterations     = cfg.iterations
        self.n_sh           = cfg.n_sh
        self.feature        = cfg.feature
        self.type           = cfg.type
        self.cl             = cfg.cl
        self.lam_orth       = lam
        self.update_func    = cfg.update_func
        self.rank_0         = rank_0
        self.rank_1         = rank_1
        self.results_path   = os.path.join(cfg.home_path, "results")
        self.H_path   = os.path.join(cfg.home_path, "H")
        self.tmp_path       = os.path.join(cfg.home_path, "tmp")
        self.csv            = cfg.csv
      
        self.results_name   = os.path.join(self.results_path, "W_"+self.feature+"_"+self.type+"_"+self.update_func+"_"+str(self.rank_1)+'p_'+str(self.rank_0)+'n_'+str(self.n_sh)+'sh_'+str(self.lam_orth)+'lam_'+self.cl+'test.txt')
        
        self.H_name   = os.path.join(self.H_path, "W_"+self.feature+"_"+self.type+"_"+self.update_func+"_"+str(self.rank_1)+'p_'+str(self.rank_0)+'n_'+str(self.n_sh)+'sh_'+str(self.lam_orth)+'lam_'+self.cl+'.p')
        
	self.H_event =  os.path.join(self.H_path, "Hevent_"+self.feature+"_"+self.type+"_"+self.update_func+"_"+str(self.rank_1)+'p_'+str(self.rank_0)+'n_'+str(self.n_sh)+'sh_'+str(self.lam_orth)+'lam_'+self.cl+'.p') 

        if not os.path.isdir(self.results_path):
            os.makedirs(self.results_path)
        
    def run(self,X_test,y_test,W):
        """ Run evaluation
        Args:
            X_test: list of test spectrograms
            y_test: list of labels
            clf:    trained classifier
            W:      trained dictionary
        Output:
            NONE, the results are saved in a file
        """   
        print("NMF of test files")
        test_list = Parallel(n_jobs=num_cores)(delayed(process_parallel)(W.shape[1], f, W0 = W, lam=self.lam_orth, iterations=self.iterations, rankW0=self.rank_0, rankW1=self.rank_1) for f in tqdm(X_test))
        # test_data_pooled =[(np.hstack((np.mean(sample[1], axis=1), np.std(sample[1], axis=1)))) for sample in test_list]
	H_event = [t[-self.rank_1:,:]for t in test_list]
        cPickle.dump(H_event, open(self.H_event, 'wb' ), protocol=cPickle.HIGHEST_PROTOCOL )
        thresh  = [0.5*np.max(t) for t in test_list]
        H_thresh = [h > thresh[i] for i, h in enumerate(H_event)]
        cPickle.dump(H_thresh, open(self.H_name, 'wb' ), protocol=cPickle.HIGHEST_PROTOCOL )
        
        event_segments = [self.contiguous_regions(np.sum(h, axis=0)>0)*cfg.win/cfg.fs for h in H_thresh]
        event_segments = [self.postprocess_event_segments(e,minimum_event_length=0.1,minimum_event_gap=0.1) for e in event_segments]
        
        # cPickle.dump(event_segments, open(self.results_name, 'wb' ), protocol=cPickle.HIGHEST_PROTOCOL )
        
        dump_file = os.path.join(self.tmp_path, self.cl+"datadump.p")
        data_dict = cPickle.load(open( dump_file, 'rb'))
        itemid_test = data_dict['itemid_test']
        
        with open(self.results_name, 'wt') as f:
	    print("Saving resluts to " + self.results_name)
            writer = csv.writer(f, delimiter='\t')
            for i, name in enumerate(itemid_test):
                if len(event_segments[i]):
                    writer.writerow([name,event_segments[i][0][0],event_segments[i][0][1],self.cl])
                else:
                    writer.writerow([name])
        
    def contiguous_regions(self,activity_array):
        # Find the changes in the activity_array
        change_indices = np.diff(activity_array).nonzero()[0]
        # Shift change_index with one, focus on frame after the change.
        change_indices = change_indices + 1
        if activity_array[0]:
            # If the first element of activity_array is True add 0 at the beginning
            change_indices = np.r_[0, change_indices]
        if activity_array[-1]:
            # If the last element of activity_array is True, add the length of the array
            change_indices = np.r_[change_indices, activity_array.size]
        # Reshape the result into two columns
        return change_indices.reshape((-1, 2))
        
    def postprocess_event_segments(self,event_segments, minimum_event_length=0.05, minimum_event_gap=0.1):
        # 1. remove short events
        event_results_1 = []
        for event in event_segments:
            if event[1]-event[0] >= minimum_event_length:
                event_results_1.append((event[0], event[1]))
        if len(event_results_1):
            # 2. remove small gaps between events
            event_results_2 = []
            # Load first event into event buffer
            buffered_event_onset = event_results_1[0][0]
            buffered_event_offset = event_results_1[0][1]
            for i in range(1,len(event_results_1)):
                if event_results_1[i][0] - buffered_event_offset > minimum_event_gap:
                    # The gap between current event and the buffered is bigger than minimum event gap,
                    # store event, and replace buffered event
                    event_results_2.append((buffered_event_onset, buffered_event_offset))
                    buffered_event_onset = event_results_1[i][0]
                    buffered_event_offset = event_results_1[i][1]
                else:
                    # The gap between current event and the buffered is smalle than minimum event gap,
                    # extend the buffered event until the current offset
                    buffered_event_offset = event_results_1[i][1]
            # Store last event from buffer
            event_results_2.append((buffered_event_onset, buffered_event_offset))
            return event_results_2
        else:
            return event_results_1    
