from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3  
import mutagen.id3  
from mutagen.id3 import ID3, TIT2, TIT3, TALB, TPE1, TRCK, TYER  
  
import glob  
  
import numpy as np  
import shutil
import os
for i in glob.glob("/media/wonho/TESLADRIVE/MUSIC/*"):
    files=glob.glob(i+'/*.mp3')
    for k in files:
#         k=k.replace('\\','/')
        mp3file=MP3(k,ID3=EasyID3)
        print(1,k)
        try:
            hiphop=False
            for genre in mp3file['genre']:
                if 'hip' in genre.lower():
                    hiphop=True
                if 'rap' in genre.lower():
                    hiphop=True
            if hiphop==False:
                artist_name= mp3file['artist']
                print(artist_name)
                for name in artist_name:
                    directory = "/media/wonho/TESLADRIVE/MUSIC2/"+name
                    print(directory)
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    file_dir=directory+'/'+k.split('/')[-1]
                    print('file_dir: ',file_dir)
                    shutil.copy(k, file_dir)
        except:
            failed_directory = "/media/wonho/TESLADRIVE/MUSIC2/failed"
            if not os.path.exists(failed_directory):
                os.makedirs(failed_directory) 
            shutil.copy(k, failed_directory+'/'+k.split('/')[-1])

for i in glob.glob("/media/wonho/TESLADRIVE/MUSIC/*"):
    files=glob.glob(i+'/*.flac')
    for k in files:
#         k=k.replace('\\','/')
        flacfile=FLAC(k) 
        
        try:
            hiphop=False
            for genre in mp3file['genre']:
                if 'hip' in genre.lower():
                    hiphop=True
                if 'rap' in genre.lower():
                    hiphop=True
            if hiphop==False:            
                artist_name= flacfile['artist']
                print(artist_name)
                for name in artist_name:
                    directory = "/media/wonho/TESLADRIVE/MUSIC2/"+name
                    print(directory)
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    file_dir=directory+'/'+k.split('/')[-1]
                    print('file_dir: ',file_dir)
                    shutil.copy(k, file_dir)
        except:
            failed_directory = "/media/wonho/TESLADRIVE/MUSIC2/failed"
            if not os.path.exists(failed_directory):
                os.makedirs(failed_directory) 
            shutil.copy(k, failed_directory+'/'+k.split('/')[-1])
