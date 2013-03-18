import os 
#import inotify

#on startup scan src dir if exists
#scan cache dir 
SRC_DIR = {}
SRC_DIR['/superfree'] = ['movies','tv_series']
CACHE_DIR = '/superfree-cache'

def scanDirectories():
    for dirName, subdirList, fileList in os.walk(SRC_DIR.keys()):
        pass
        
        


if "__name__" == "__main__":
    pass
    #inotify wait here..
