import numpy as np
import config as cfg
import pickle
import matplotlib.pyplot as plt
from IPython.core.debugger import Tracer

def contiguous_regions(activity_array):
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
    
def postprocess_event_segments(event_segments, minimum_event_length=0.05, minimum_event_gap=0.1):
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

H_thresh=pickle.load(open('/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/16000/H/W_mel_01_orth_eucl_10p_50n_4sh_1000lam_gunshot.p', 'rb'))
H_thresh_orth=pickle.load(open('/vol/vssp/AcousticEventsDetection/DCASE2017-baseline-system/applications/data/TUT-rare-sound-events-2017-development/16000/H/W_mel_01_orth_kls_10p_50n_4sh_1000lam_gunshot.p', 'rb'))

Tracer()()

#start=0

#for i in xrange(start,start+5):
#    plt.figure();plt.imshow(H_thresh[i], aspect='auto'); plt.title("baseline"); plt.show()
#    plt.figure();plt.imshow(H_thresh_orth[i], aspect='auto'); plt.title("orth"); plt.show()
#    plt.figure();plt.plot(np.sum(H_thresh[i], axis=0)); plt.title("baseline"); plt.show()
#    plt.figure();plt.plot(np.sum(H_thresh_orth[i], axis=0)); plt.title("orth"); plt.show()
#    event_segments = contiguous_regions(np.sum(H_thresh[i], axis=0)>0)*cfg.win/cfg.fs
#    event_segments = postprocess_event_segments(event_segments,minimum_event_length=0.1,minimum_event_gap=0.1) 
#    event_segments_orth = contiguous_regions(np.sum(H_thresh_orth[i], axis=0)>0)*cfg.win/cfg.fs 
#    event_segments_orth = postprocess_event_segments(event_segments_orth,minimum_event_length=0.1,minimum_event_gap=0.1)
#    print i, event_segments, event_segments_orth
    
#plt.close('all')
