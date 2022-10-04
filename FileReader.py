from operator import index, indexOf
import sys
from Logger import LogLinks
from song import Download
from Searcher import FindSong
author = ""


def Read():
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
                Download(youtubeLink, author, line)
                LogLinks(youtubeLink)
    return 0
