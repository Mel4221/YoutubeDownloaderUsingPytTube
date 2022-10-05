from FileReader import Read,ReadCompleteFile
from Logger import Log
from Options import Selector

def Main():
          #ReadCompleteFile()
          #print("Please type the name of the list that you will be downloading from")
          #list = input()
          #Read(list)
          #Tester()
          Selector()
          Log(file="LastExit",matter="This was the last exit from the application",ext=".log")
          return 0
Main()
 
