# Load imports
import os 
import pandas as pd
import numpy as np

def get_keystrokes(keystroke_directory, k, k2):
    X1 = []
    y1 = []
    
    X2 = []
    y2 = []
    
    retrieve_headers = False
    subfolders = os.listdir(keystroke_directory)
    for subfolder in subfolders: #for each subject
        # print("Loading keystroke data in %s" % subfolder)
        if os.path.isdir(os.path.join(keystroke_directory, subfolder)): 
            subfolder_files = os.listdir(
                    os.path.join(keystroke_directory, subfolder)
                    )
            for file in subfolder_files: #for each session that matches given k
                if file == 'Session%d.csv' % k:
                  
                    session = pd.read_csv(os.path.join(keystroke_directory, subfolder, file), usecols = lambda x: x[0] == 'H')
                                    
                    if retrieve_headers == False:
                        headers = session.columns.tolist()
                        retrieve_headers = True
                        
                    X1.append(session.to_numpy())
                    y1.extend([subfolder] * len(session.index)) #subfolder name
                    
            # ----------------------------------------
                    
            for file in subfolder_files: #for each session that matches given k2
                if file == 'Session%d.csv' % k2:
                  
                    session = pd.read_csv(os.path.join(keystroke_directory, subfolder, file), usecols = lambda x: x[0] == 'H')
                                          
                    X2.append(session.to_numpy())
                    y2.extend([subfolder] * len(session.index))
     
    return np.vstack(X1), np.array(y1), np.vstack(X2), np.array(y2), headers 
    #returns everyone's session1 vs session2, session1 vs session3, etc. stacked


            