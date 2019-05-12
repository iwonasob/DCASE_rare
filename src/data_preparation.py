'''
Prepares the data for training and testing
'''
import config as cfg
import os
import pandas as pd
import cPickle
import numpy as np
import librosa
from IPython.core.debugger import Tracer

class DataPreparation:
    def __init__(self,
                 datasets
                 ):
                     
        """ Initialize class
        Args:
            datasets (list): List of datasets to use
        """
        self.datasets   = datasets
        self.tmp_path   = os.path.join(cfg.home_path, "tmp")
        self.n_sh       = cfg.n_sh
        self.csv        = cfg.csv
        self.cl         = cfg.cl
        
        if not os.path.isdir(self.tmp_path):
            os.makedirs(self.tmp_path)
            
    def run(self):
        '''
        Creates or loads data used for training and testing
        '''
        dump_file = os.path.join(self.tmp_path, self.cl+"datadump.p")
        if not os.path.isfile(dump_file): 
            data_dict = {}
            [data_dict['X_train'], data_dict['y_train'], data_dict['itemid_train']]=self.load_data(self.datasets[0])   
            [data_dict['X_test'], data_dict['y_test'], data_dict['itemid_test']]=self.load_data(self.datasets[1])
            cPickle.dump( data_dict, open( dump_file, 'wb'), protocol=cPickle.HIGHEST_PROTOCOL )
            print("Training and test data saved to: " + dump_file)
        else:
            data_dict = cPickle.load(open( dump_file, 'rb'))
            print("Loaded the training and test data from: " + dump_file)
        X_train, y_train, itemid_train, X_test,  y_test, itemid_test = data_dict['X_train'], data_dict['y_train'], data_dict['itemid_train'], data_dict['X_test'], data_dict['y_test'], data_dict['itemid_test']
        X_train_1 = self.preprocess_data([X_train[i] for i in np.where(np.array(y_train)==1)[0]])
        X_train_0 = self.preprocess_data([X_train[i] for i in np.where(np.array(y_train)==0)[0]])
        X_test = self.preprocess_data(X_test) 
	return [X_train_1, X_train_0, X_test, y_test]
            
        
    def preprocess_data(self, data):
        ''' Normalise and shingle data
        Args:
            data: list containing the spectrograms
        '''
        data_norm=[ t/np.max(t) for t in data]
        data_sh=[librosa.feature.stack_memory(t.transpose(), n_steps=self.n_sh) for t in data_norm]
        return data_sh
        

    def load_data(self, dataset):
        ''' Load selected data
        Args:
            dataset:    name of the dataset 
            fold_n:     number of the partition fold
        '''
        print("Loading dataset " + dataset)
        csv_path=os.path.join(cfg.home_path, dataset, self.csv)
        data = pd.read_csv(csv_path,delimiter="\t")
        label=data['label'].values
        itemid=data['name'].values
        paths=[os.path.join(cfg.home_path, dataset, cfg.feature, i+".f") for i in itemid]
        X = [cPickle.load(open(path, 'rb')) for path in paths]
	return [X, label, itemid]
