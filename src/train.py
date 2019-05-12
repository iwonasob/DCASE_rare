'''
Train the dictionary and a classfier
'''

import config as cfg
import os
import numpy as np
import cPickle
from sklearn import  ensemble
from joblib import Parallel, delayed
import multiprocessing
from nmf import NMF, process_parallel

np.random.seed(1515)
eps = np.spacing(1)
num_cores = multiprocessing.cpu_count()

class Trainer:
    def __init__(self,
                lam,
                rank_0,
                rank_1):
                     
        """ Initialize class
        """
        self.lam_orth       = lam
        self.n_sh           = cfg.n_sh
        self.feature        = cfg.feature
        self.type           = cfg.type
        self.cl             = cfg.cl
        self.update_func    = cfg.update_func
        self.iterations     = cfg.iterations
        self.rank_0         = rank_0
        self.rank_1         = rank_1
        self.n_trees        = cfg.n_trees
        self.H_path         = os.path.join(cfg.home_path, "H")
        self.W_path         = os.path.join(cfg.home_path, "W")
        self.clf_path       = os.path.join(cfg.home_path, "clf")

        self.W_name         = os.path.join(self.W_path, "W_"+self.feature+"_"+self.type+"_"+self.update_func+"_"+str(self.rank_1)+'p_'+str(self.rank_0)+'n_'+str(self.n_sh)+'sh_'+str(self.lam_orth)+'lam_'+self.cl+'norm.p')
        
        self.H_name         = os.path.join(self.H_path, "H_"+self.feature+"_"+self.type+"_"+self.update_func+"_"+str(self.rank_1)+'p_'+str(self.rank_0)+'n_'+str(self.n_sh)+'sh_'+str(self.lam_orth)+'lam_'+self.cl+'.p')
        
        self.clf_name         = os.path.join(self.W_path, "W_"+self.feature+"_"+self.type+"_"+self.update_func+"_"+str(self.rank_1)+'p_'+str(self.rank_0)+'n_'+str(self.n_sh)+'sh_'+str(self.lam_orth)+'lam_'+self.cl+'.p')
        
        if not os.path.isdir(self.W_path):
            os.makedirs(self.W_path)
            
        if not os.path.isdir(self.H_path):
            os.makedirs(self.H_path)
            
        if not os.path.isdir(self.clf_path):
            os.makedirs(self.clf_path)
        
    def run_nmf(self,tr_positive,tr_negative):
        '''Extract a dictionary via NMF given a method chosen in config file
        Args:
           tr_positive: a numpy array containing all the positive examples 
           tr_negative: a numpy array containing all the negative examples
        Output:
            NONE, the dictionary is saved in a file
        '''
        print(tr_positive.shape)
        if self.type == '0_1':
            
            print("NMF on positive examples")
            nmf_model=NMF(self.rank_1, norm_W=1,  iterations=self.iterations, update_func = self.update_func, verbose=True)
            [W_positive,H,error]=nmf_model.process(tr_positive)
            
            print("NMF on negative examples")
            nmf_model=NMF(self.rank_0, norm_W=1,  iterations=self.iterations, update_func = self.update_func, verbose=True)
            [W_negative,H,error]=nmf_model.process(tr_negative)
            
            print("Saved dictionary to "+self.W_name)
            W=np.hstack((W_positive,W_negative))
            cPickle.dump( [W_positive, W_negative], open( self.W_name, 'wb' ), protocol=cPickle.HIGHEST_PROTOCOL )
        
        elif self.type == 'unsupervised':
            
            print("Unsupervised NMF")
            V=np.hstack((tr_negative,tr_positive))
            nmf_model=NMF(self.rank_0+self.rank_1, norm_W=1,  iterations=self.iterations, update_func = self.update_func, verbose=True)
            [W,H,error]=nmf_model.process(V) 
            
            print("Saved dictionary to "+self.W_name)
            cPickle.dump( W, open( self.W_name, 'wb' ), protocol=cPickle.HIGHEST_PROTOCOL )
            
        elif self.type == '01':
            # # -------- Train with masking ----------
            print("Masked NMF on training files")
            V=np.hstack((tr_negative,tr_positive))
            
            mask=np.zeros((self.rank_1, tr_negative.shape[1]))
            H0=np.random.rand(self.rank_0+self.rank_1, V.shape[1])+eps
            H0[-mask.shape[0]:,:mask.shape[1]]=mask
            
            nmf_model=NMF(self.rank_0+self.rank_1, norm_W=1,  iterations=self.iterations, update_func = self.update_func, verbose=True)
            [W,H,error]=nmf_model.process(V,H0=H0) 
            
            print("Saved dictionary to "+self.W_name)
            cPickle.dump( W, open( self.W_name, 'wb' ), protocol=cPickle.HIGHEST_PROTOCOL )
            
            
        elif self.type == '01_orth':
            # # -------- Train with masking ----------
            print ("masked NMF on training files")
            V=np.hstack((tr_negative,tr_positive))
            
            mask=np.zeros((self.rank_1, tr_negative.shape[1]))
            H0=np.random.rand(self.rank_0+self.rank_1, V.shape[1])+eps
            H0[-mask.shape[0]:,:mask.shape[1]]=mask
            
            nmf_model=NMF(self.rank_0+self.rank_1, norm_W=1, rankW0 = self.rank_0, rankW1 = self.rank_1, len_V0 = tr_negative.shape[1],  iterations=self.iterations, update_func = self.update_func, verbose=False)
            print(self.lam_orth)
            [W,H,error]=nmf_model.process(V,H0=H0, lam_orth=self.lam_orth) 

            print("Saved dictionary to "+self.W_name)
            cPickle.dump( W, open( self.W_name, 'wb' ), protocol=cPickle.HIGHEST_PROTOCOL )
        else:
            raise ValueError('Dictionary type not recognized')
         
        return W
            
            
            
    def run_rf(self,tr_positive,tr_negative):
        ''' Extracts activation matrices using a trained dictionary. Tains a classifier on pooled activations.
        Args:
           tr_positive: a numpy array containing all the positive examples 
           tr_negative: a numpy array containing all the negative examples
        Output:
            clf:    trained classifier
            W  :    used dictionary
        '''
        
        print "Loading dictionary "+ self.W_name
        if self.type == '01' or self.type == '01_orth' or self.type =='unsupervised':
            W = cPickle.load(open(self.W_name, 'rb' ))
        elif self.type == '0_1':
            [W_positive,W_negative] = cPickle.load(open(self.W_name, 'rb'))
            W=np.hstack((np.vstack(W_positive),np.vstack(W_negative)))
        else:
            raise ValueError('Dictionary type not recognized')
        
        print("NMF of training files")
        train_data = tr_positive + tr_negative
        train_label=np.hstack([np.ones(len(tr_positive)),np.zeros(len(tr_negative))])
        train_list = Parallel(n_jobs=num_cores)(delayed(process_parallel)(W.shape[1], f, W0 = W,  iterations=self.iterations) for f in train_data)
        cPickle.dump( train_list, open( self.H_name, 'wb' ), protocol=cPickle.HIGHEST_PROTOCOL )
        data_pooled =[(np.hstack((np.mean(sample[1], axis=1), np.std(sample[1], axis=1)))) for sample in train_list]
        
        print("Training Random Forest")
        clf =ensemble.RandomForestClassifier(self.n_trees, n_jobs=-1)
        clf.fit(np.array(data_pooled), train_label)
        print("Saved classifier to "+self.clf_name)
        cPickle.dump( clf, open( self.clf_name, 'wb' ), protocol=cPickle.HIGHEST_PROTOCOL )
        return [clf, W]
