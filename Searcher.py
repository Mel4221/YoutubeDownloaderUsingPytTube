from Logger import Log
import sys
from pytube import Search
from pytube import YouTube
from song import Fails, PrintStatus

# this finds the song's link using the name provided
searchData = ""


def FindSong(song):
   # try:
   
   
                    songName = song     
                    print("Finding Link for : "+songName) 
                    if songName.find("http") >=0:
                              songName = songName[songName.index('=')+1:len(songName)-1]
                    #print("Finally: "+songName)
                    
                    s  = Search(songName)
                    youTubeLink = "https://www.youtube.com/watch?v="
                    listOfLinks = str(s.results[0])
                    ida = listOfLinks.index('=')+1
                    idb = listOfLinks.index('>')
                    firstVideoId = listOfLinks[ida:idb]
                    video = youTubeLink+firstVideoId
                    print("Link Founded : "+video)
                    global searchData
                    searchData = video
                    #input()
                    return video
                            
    #except:

