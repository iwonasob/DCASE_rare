import sed_eval

from IPython.core.debugger import Tracer

cl="gunshot"

file_list = [
    # {
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE_task2/mixed_audio/testing/list_"+cl+"_gt.txt",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE_task2/mixed_audio/results/W_mel_01_kls_10p_50n_4sh_1000lam_"+cl+".txt"
    # },
    # {
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_10n_4sh_500lam_gunshot.txt"
    # },
    # {   
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_10n_4sh_500lam_gunshot.txt"
    # },
    # {
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_10n_4sh_5000lam_gunshot.txt"
    # },
    # {   
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_10n_4sh_5000lam_gunshot.txt"
    # },
    # {
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_100n_4sh_500lam_gunshot.txt"
    # },
    # {   
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_100n_4sh_500lam_gunshot.txt"
    # },
    # {
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_50n_4sh_500lam_gunshot.txt"
    # },
    # {   
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_50n_4sh_500lam_gunshot.txt"
    # },
    # {
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_50n_4sh_1000lam_gunshot.txt"
    # },
    # {   
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_50n_4sh_1000lam_gunshot.txt"
    # },
    # {
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_50n_4sh_1000lam_gunshot.txt"
    # },
    # {   
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_50n_4sh_1000lam_gunshot.txt"
    # },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_20p_10n_4sh_0lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_20p_10n_4sh_500lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_10n_4sh_0lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_10n_4sh_500lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_10n_4sh_0lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_10n_4sh_500lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_50n_4sh_0lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_eucl_10p_50n_4sh_100lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_50n_4sh_0lam_gunshotold.txt"
    },  
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_eucl_orth_10p_50n_4sh_0lam_gunshotold.txt"
    },   
    
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_50n_4sh_0lam_gunshotnorm.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_10p_50n_4sh_1000lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_50n_4sh_500lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_50n_4sh_0lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_50n_4sh_500lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_50n_4sh_500lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_50n_4sh_1000lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_50n_4sh_5000lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_20p_100n_4sh_0lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_20p_100n_4sh_500lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_20p_100n_4sh_500lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_20p_100n_4sh_1000lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_20p_100n_4sh_5000lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_20n_4sh_0lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_20n_4sh_500lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_20n_4sh_1000lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_10p_20n_4sh_5000lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_20n_4sh_0lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_20n_4sh_500lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_20n_4sh_1000lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_10p_20n_4sh_5000lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_5p_20n_4sh_0lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_5p_20n_4sh_500lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_5p_20n_4sh_1000lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kl_orth_5p_20n_4sh_5000lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_5p_20n_4sh_0lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_5p_20n_4sh_500lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_5p_20n_4sh_1000lam_gunshot.txt"
    },
    {   
     'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
     'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_eucl_orth_5p_20n_4sh_5000lam_gunshot.txt"
    },

  # {
    #  'reference_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/mixtures_devtest_0367e094f3f5c81ef017d128ebff4a3c/list_"+cl+"_gt.csv",
    #  'estimated_file': "/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/generated_data/results/W_mel_01_orth_kls_10p_50n_4sh_10000lam_"+cl+".txt"
    # },



]

data = []

# Get used event labels
all_data = sed_eval.util.event_list.EventList()
event_labels = all_data.unique_event_labels
for file_pair in file_list:
    print(file_pair['estimated_file'])
    reference_event_list = sed_eval.io.load_event_list(file_pair['reference_file'])
    # Tracer()()
    estimated_event_list = sed_eval.io.load_event_list(file_pair['estimated_file'])
    data.append({'reference_event_list': reference_event_list,
                 'estimated_event_list': estimated_event_list})
    all_data += reference_event_list


# Start evaluating

# Create metrics classes, define parameters
# segment_based_metrics = sed_eval.sound_event.SegmentBasedMetrics(event_label_list=event_labels,
                                                                 # time_resolution=1)
    event_based_metrics = sed_eval.sound_event.EventBasedMetrics(event_label_list=[0,1],t_collar=0.5,percentage_of_length=0.5,evaluate_onset=True, evaluate_offset=False)
    
    # Go through files
    for file in reference_event_list.unique_files:
        # Get reference event list for file by filtering reference_event_list
        reference_event_list_for_current_file = reference_event_list.filter(file=file)
        # Get estimated event list for file by filtering estimated_event_list
        estimated_event_list_for_current_file = estimated_event_list.filter(file=file)
        event_based_metrics.evaluate(
            reference_event_list=reference_event_list_for_current_file,
            estimated_event_list=estimated_event_list_for_current_file
        )
    print(event_based_metrics.results_overall_metrics())
    




