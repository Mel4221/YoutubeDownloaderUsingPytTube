from multiprocessing.dummy import Array
import sys
import regex
from datetime import datetime
from pathlib import Path
import os
from pytube import YouTube
from Searcher import FindSong
from array import array


     
def GetVideo():
          print("Downloading Video")
          videoLink = FindSong("yo soy tu gominola")
          yt = YouTube(videoLink)
          #print("Youtube Link: "+videoLink)
          """
                    Now im trying to work with the metadata or anything
                    that can give's me more details about how this is working right this moment
          """ 
          
          
def Tester():
          GetVideo()
     