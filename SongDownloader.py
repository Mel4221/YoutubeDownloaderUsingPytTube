import sys
import tempfile
import moviepy.editor as mp
import regex
from datetime import datetime
from pathlib import Path
import os
from pytube import YouTube
from Searcher import FindSong
from array import array


DownloadDir = Path("downloads")
  
def DownloadSong(song, authorName, songName):
   #try:      
          
          videoLink = song #FindSong("yo soy tu gominola")
          yt = YouTube(videoLink)
          clearName = regex.sub(r'[^\w]', ' ',authorName)
          author = clearName.replace(" ","")
          fileName = "temp.mp4" #regex.sub(r'[^\w]', ' ',yt.title)
          
          authorDir = Path(author)
          path = str(DownloadDir)+"/"+str(authorDir)
          pathWithFile = path+"/"+fileName
         
          
          if DownloadDir.is_dir()==False :
                    print("Creatting Download Folder")
                    try:
                              os.mkdir(DownloadDir)
                    except:
                              print("..........................")
                        
          if authorDir.is_dir()==False :
                    print("Creatting Author Folder '"+str(author)+"'")
                    try:
                              os.mkdir(path)
                    except:
                              print("..........................")
    
          #Download File
          tempFile = Path(path+"/"+fileName)
          
          if tempFile.is_file()==True:
                    try:
                              os.remove(pathWithFile)
                    except:
                              print("..........................")
                    
          print("Downloading Video "+songName)
          filter = yt.streams.filter(file_extension='mp4').get_lowest_resolution().download(output_path=path+"/", filename=fileName, filename_prefix="",
                    skip_existing=True, timeout=10000, max_retries=10)
          
          print("Downloaded Completed!!!")
          print(filter)
          print("Converting mp4 to mp3")
          
          mp4 = mp.VideoFileClip(pathWithFile)
          
          mp3 = regex.sub(r'[^\w]', ' ',yt.title).replace(" ","_")#making the name a safe name for any system
          print(mp3)
          mp4.audio.write_audiofile(path+"/"+mp3+".mp3")
          print("Convertion Completed!!!")
          print("Deleting Temporal File")
          os.remove(pathWithFile)
          print("Completed!!!")
          #os.makedirs("downloads/temp")
          
   #except:
    #      print("Error Type")
          #print("Please Press Enter")
          #input()
          """
                    Now im trying to work with the metadata or anything
                    that can give's me more details about how this is working right this moment
          """ 
          

        
 
def Tester():
          GetVideo()
          
          
          
     