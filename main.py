import sys
import subprocess
from FileReader import Reader



def Main():
          
       #Reader()
       subprocess.Popen("mono Ext.exe", shell=True, stdout=subprocess.PIPE).stdout.read()
       return
 
