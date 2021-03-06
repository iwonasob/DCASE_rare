'''
Configuration file containing all the parameters of the system
'''

# MODE
mode="dev" # 'dev' for training and testing on 10% of the data, 'eval' to train on the entire dataset

# PATHS
#home_path   = "/vol/vssp/AcousticEventsDetection/DCASE_task2/mixed_audio"
home_path= "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/"
cl ="babycry"
#cl ="glassbreak"  
# cl ="gunshot"                     
csv= "list_"+cl+".csv"

# global params
feature ="mel"
win     = 1024
fs      = 16000.
n_mels  = 40
n_sh    = 4     # number of shingles, i.e. concatenated frames

# NMF training parameters
type        = '01_orth' #'01' for masked NMF, '0_1' for class-conditioned NMF, 'unsupervised' for unsupervised NMF
update_func = "kl_orth"
lam_orth    = 1000
iterations  = 500
rank_0      = 20    # rank of negative dictionary
rank_1      = 10   # rank of positive dictionary

# Classifier paramters
n_trees = 500       # number of trees in a random forest
