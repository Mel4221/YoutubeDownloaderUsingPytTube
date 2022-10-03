import sys
from pytube import Search
from pytube import YouTube

          #this finds the song's link using the name provided
def FindSong(songName):
          s = Search(songName)
          youTubeLink = "https://www.youtube.com/watch?v="
          listOfLinks = str(s.results[0])
          ida = listOfLinks.index('=')+1
          idb = listOfLinks.index('>')
          firstVideoId = listOfLinks[ida:idb]
          video = youTubeLink+firstVideoId
          return video
# print(listOfLinks)  # for testing
# print(firstVideoId)
# Final Video with the link
