import sys
from pathlib import Path
from console import Clear
import os
from pytube import YouTube
#from builtins import str

n = 0
errors = 0
completed = 0


def Download(song, author, songName):

    try:
        Video = song
        down = "downloads/"
        downPath = Path(down)
        if downPath.is_dir() == False:
            os.mkdir(downPath)

        authorDir = Path(down+author)
        if authorDir.is_dir() == False:
            os.mkdir(authorDir)

        path = os.path.join(down, author)
        yt = YouTube(Video)
        print(yt.title)
        lst = yt.streams.filter()
        for v in lst:
            Clear()
            print("Downloading "+songName)
            print("Completed "+str(completed) + " "+"Failed "+str(errors))

        vtag = yt.streams.filter(only_audio=True).get_audio_only().itag

        file = stream.download(output_path=path, filename=".mp3", filename_prefix=yt.title,
                               skip_existing=True, timeout=10000, max_retries=10)
        
        print("File Location: "+file+" Downloaded Completed!!!")
    
        print(yt.title)
   
        completed + 1

    except:
        errors + 1

    #print("Waiting for an input")
    #text = input()

        #  yt.streams.get_by_itag(vtag).download(out_path="downloads/",filename="test.mp4")
