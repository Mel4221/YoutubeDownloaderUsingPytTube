from operator import index, indexOf
import sys
from Logger import LogLinks
from song import Download
from Searcher import FindSong
from SongDownloader import DownloadSong
import os 
author = ""


def Read():
 try:
    print("Reading List")
    with open('list.txt') as f:
        for line in f:
            if line.find(':') > 0:
                author = line.replace(':', '')
                print("Author: "+line)
            else:
                songName = author.replace(':', '')+" "+line+" letra"
                print(songName)
                print("Finding Link...")
                youtubeLink = FindSong(songName)
                #Download(youtubeLink, author, line)
                DownloadSong(youtubeLink,author,songName)
                LogLinks(youtubeLink)
                return 0 
 except:
           print("Please try to put the list inside the list.txt file")
           os.mkfifo("list.txt")
           
           return 1