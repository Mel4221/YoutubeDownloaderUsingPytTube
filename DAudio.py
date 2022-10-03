import sys
from pytube import YouTube
#from builtins import str


def DAudio():
         var="I don't know , but i will know why eventually this variable is litterally doing nothing but for some reason if i remove it it does not work"
Video="https://www.youtube.com/watch?v=93mdB3_GgSo"
yt=YouTube(Video)
print(yt.title)
lst = yt.streams.filter()
for v in lst:
          print("Downloading...")
          vtag=yt.streams.filter(only_audio=True).get_audio_only().itag
          #print(vtag)
          stream = yt.streams.get_by_itag(vtag)
          stream.download()
          
        #  yt.streams.get_by_itag(vtag).download(out_path="downloads/",filename="test.mp4")
          
DAudio()
          
          
