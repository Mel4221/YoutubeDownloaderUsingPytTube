from datetime import datetime
       
def LogLinks(links):
          now = datetime.now()
          time = now.strftime("%H:%M:%S")
          file1 = open("data/LINKS"+time+".log","w")
          L = [links]
          file1.writelines(L)
          file1.close()
          
def Log(file,matter):
          now = datetime.now()
          time = now.strftime("%H:%M:%S")
          file1 = open(file+".log","w")
          L = [time,matter]
          file1.writelines(L)
          file1.close()