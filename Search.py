import sys
from pytube import Search
from pytube import YouTube

#testing variables
s = Search('René Gonzales Tú presencia letra')
#default link from youtube
youTubeLink = "https://www.youtube.com/watch?v="
#getting the first video from the list
listOfLinks = str(s.results[0])

#selection only the ID from the first video
ida =  listOfLinks.index('=')+1
idb = listOfLinks.index('>')

firstVideoId = listOfLinks[ida:idb]
print(listOfLinks) #for testing
print(firstVideoId)

#Final Video with the link
finalLink = youTubeLink+firstVideoId

