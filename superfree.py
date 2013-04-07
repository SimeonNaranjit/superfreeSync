#!/usr/bin/env python3

import os 
import subprocess
import re
#import inotify

#on startup scan src dir if exists
#scan cache dir 
SRC_DIR = {}
SRC_DIR['/mnt/superfree'] = ['movies','tv_series']
CACHE_DIR = '/mnt/superfree-cache'
TIME_IN_DAYS = 30
FILE_PERCENT = 10

def scanDirectories():
    sourceDir = SRC_DIR.keys()[0]
    for root, dirs, files in os.walk(CACHE_DIR):
        dirs[:] = SRC_DIR['/superfree']
        #skip hidden directories
        dirs[:] = [d for d in dirs if not d[0] == '.']
        if os.path.exists(root.replace(sourceDir,CACHE_DIR,1))
            pass
            print('exists')
        else:
            if os.path.isfile(root):
                f = os.stat(root)
                if f.st_atime(root) > TIME_IN_DAYS * 86400:
                    copyFilePercent(root)
            rsyncFile(sourceDir,CACHE_DIR)

        print(root)

def getFileDuration(filename):
    ffmpeg = "ffmpeg -i"
    ffmpegOut = subprocess.check_output([ffmpeg,filename],shell=True)
    for line in ffmpegOut.split('\n'):
        match = re.search('[0-9][0-9]:[0-9][0-9]:[0-9][0-9]\.[0-9][0-9]',ffmpegOut)
        if match:
            duration = match.group()
            return duration

def getSec(s):
    l = s.split(':')
        return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

def getTime(secomds):
    

def getFilePercentages(duration):
    seconds = getSec(duration)
    if seconds > 300:
        firstLength = 300:
    if seconds > 1200:
        sencondLength = 
        

        
         
def copyFilePercent(filename):
    fileSize = os.path.getsize(filename)
    filePercentSize = fileSize * float("." + FILE_PERCENT)
    duration = getFileDuration(filename)
    subprocess.(head --bytes=%s %s % filePercentSize
    
    
if __name__ == "__main__":
    scanDirectories()
    #inotify wait here..
