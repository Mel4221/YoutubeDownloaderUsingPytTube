import sys
from pathlib import Path
from console import Clear
import os
from pytube import YouTube
#from builtins import str

n = 0
def Download(song,author,songName):
          
         
          
          
          Video=song
          down = "downloads/"
          downPath = Path(down)
          if downPath.is_dir()==False:
                    os.mkdir(downPath)
                    
          path = os.path.join(down,author)
          
          authorDir = Path(path)
          if authorDir.is_dir()==False:
                     os.mkdir(authorDir)

                     
          yt=YouTube(Video)
          print(yt.title)
          lst = yt.streams.filter()
          for v in lst:
                    Clear()                              
          print("Downloading "+songName)
          print("Completed "+str(n))
                    
          vtag=yt.streams.filter(only_audio=True).get_audio_only().itag
          #print(vtag)
          oldExt = ".mp4"
          newExt = ".mp3"
          file=path+yt.title
          stream = yt.streams.get_by_itag(vtag)
          check = Path(file)
          print(check+" "+file+" "+author+" "+songName)
          input()
          if check.is_file() == False:
                    stream.download(output_path = path)
                    print(yt.title)
                    os.rename(os.path.join(file,oldExt),os.path.join(file,newExt)) 
                    n+1     
          else:
                    print(file+" Downloaded Already!!!")
          

          #print("Waiting for an input")
          #text = input()
          
        #  yt.streams.get_by_itag(vtag).download(out_path="downloads/",filename="test.mp4")
          
          
          
