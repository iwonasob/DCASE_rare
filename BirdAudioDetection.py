'''
Main script to download and prepare the data and run Bird Audio Detection
'''

import config as cfg
#from src.dataset import * 
from src.feature_extraction import *
from src.data_preparation import *
from src.train import *
from src.evaluate import *
import numpy as np


from IPython.core.debugger import Tracer

if __name__ == "__main__":
    

    datasets=['training','testing']
    
    for dataset_name in datasets:
        feature_extractor = FeatureExtraction(dataset_name)
        feature_extractor.run()
        
    data_preparation = DataPreparation(datasets)
    [X_train_1, X_train_0, X_test, y_test] = data_preparation.run()
    #for lam in [500,1000,5000]:
    for lam in [1000]:
        #for rank_0 in [10,20,50,100]:
        #   for rank_1 in [5,10,20]:
                #W_pickle="/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/16000/W/W_mel_01_orth_kls_"+str(rank_1)+"p_"+str(rank_0)+"n_4sh_"+str(lam)+"lam_gunshot.p"
#        W_kl="/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/W/W_mel_01_orth_kl_orth_10p_20n_4sh_1000lam_gunshot.p"
	rank_0=20
	rank_1=10
	trainer = Trainer(lam, rank_0, rank_1)
        W = trainer.run_nmf(np.hstack(X_train_1),np.hstack(X_train_0))
 #       W =  cPickle.load(open( W_kl, 'rb'))
                
        evaluator = Evaluator(lam, rank_0, rank_1)
        evaluator.run(X_test, y_test, W)
   

    


    
        
