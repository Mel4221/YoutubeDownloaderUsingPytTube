import sys
import regex
from datetime import datetime
from Logger import AddDone, AddFail, Fail,Completed
from pathlib import Path
from console import Clear
import os
from pytube import YouTube
#from builtins import str



def Download(song, author, songName):
          try:
                    Video = song
                    down = "downloads"
                    downPath = Path(down)
                    if downPath.is_dir() == False:
                                        os.mkdir(downPath)

                    authorDir = Path(down+author)
                    if authorDir.is_dir() == False:
                                        os.mkdir(authorDir)

                    path = os.path.join(down, author)
                    yt = YouTube(Video)
                    print(yt.title)
                    yt.streams.filter()
                    Clear()
                    print("Downloading "+songName)
                    print("Completed "+str(Completed) + " "+"Failed "+str(Fail))
                    vtag = yt.streams.filter(only_audio=True).get_audio_only().itag
                    stream  = yt.streams.get_by_itag(vtag)
                    print("wait"+str(vtag))
                    #input()
                    
                    file = stream.download(output_path=path, filename=".mp3", filename_prefix=regex.sub(r'[^\w]', ' ',yt.title ),
                               skip_existing=False, timeout=10000, max_retries=10)
        
                    print("File Location: "+file+" Downloaded Completed!!!")
    
                    print(yt.title)
   
                    AddDone()

          except:
                    AddFail()
                    now = datetime.now()
                    time = now.strftime("%H:%M:%S")
                    file1t = open("data/error"+time+".log","w")
                    file1t.writelines(song)
                    file1t.close()