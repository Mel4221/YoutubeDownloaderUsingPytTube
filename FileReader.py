import sys
from song import Download
from Searcher import FindSong
author = ""
def Reader():
          var="god knows what"
          
         
with open('list.txt') as f:
    for line in f:
          if line.find(':')>0:
                    author = line.replace(':','')
                    print("***"+line+"***")
          else:
                    songName = author.replace(':','')+" "+line+" letra" 
                    print(songName)
                    youtubeLink = FindSong(songName)
                    Download(youtubeLink,author,line)
                    
