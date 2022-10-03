from pytube import YouTube
#from builtins import str


SavePath="/home/mel/Documents/python/Dpy/"
Video="https://www.youtube.com/watch?v=93mdB3_GgSo"

try:

          yt=YouTube(Video)
          
          print(yt.title)
          
          lst = yt.streams.filter()
          for v in lst:
                    print(v)
          vtag=yt.streams.filter(progressive=True).get_highest_resolution().itag
          
          #try to download it
          yt.streams.get_by_itag(vtag).download(out_path=Save_Path,filename="test.mp4")
          
except:
          print("Error While Downloading the video")
        