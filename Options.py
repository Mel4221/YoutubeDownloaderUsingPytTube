from shelve import Shelf
from console import Clear
import shutil
import os 
import FileReader
from SongDownloader import DownloadSong

def Selector():
          print("Please Type the option's Number then press Enter")
          print("0. To Exit")
          print("1. Dowanload Songs Using a list.txt file")
          print("2. Check The list File")
          print("3. Download With Links")
          print("4. Quick Download")
          print("5. Delete All Downloads")
          option=input()
          if option == '0':
                    return
          if option == '1':
                    print("Type the name of the list if nothing it will be read list.txt as default ")
                    read=input()
                    if read=="":
                              read = "list"
                              FileReader.Read(read)
                    else:
                              FileReader.Read(read)
          if option == '2':
                    print("Type the name of the list if nothing it will be read list.txt as default")
                    read=input()
                    if read=="":
                              read = "list"
                              FileReader.ReadCompleteFile(read)
                    else:
                              FileReader.ReadCompleteFile(read)
          if option == "3":
                    print("Type the name of the list if nothing it will be read list.txt as default")
                    read=input()
                    if read=="":
                              read = "list"
                              FileReader.ReadLinks(read)
                    
                    else:
                              FileReader.ReadLinks(read)
          if option == "4":
                    print("Paste the link from the video and  Press Enter")
                    link = input()
                    DownloadSong(link,"","")
          if option == "":
                    Clear()
                    Selector()
          if option == '5':
                    print("You will not be able to undo this are you sure???")
                    sure = input("y / n \n")
                    if sure == "y":
                             
                              shutil.rmtree("downloads", ignore_errors=False, onerror=None)
                              os.mkdir("downloads")
                              Clear()
                              print("downloads Folder Deleted")
                              Selector()
                    else:
                              print("Deletion Was Cancelled")
                              Selector()