from pytube import YouTube

def Downloader():       
 YouTube('https://www.youtube.com/watch?v=93mdB3_GgSo').streams.first().download()
 yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
 yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
 
 Downloader()
