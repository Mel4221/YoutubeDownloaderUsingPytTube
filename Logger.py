from datetime import datetime

Fail = 0
Completed = 0


def AddDone():
          global Completed
          Completed = Completed + 1

def AddFail():
          global Fail
          Fail = Fail +1

def LogLinks(links):
          now = datetime.now()
          time = now.strftime("%H:%M:%S")
          file1 = open("data/LINKS"+time+".log","w")
          L = [links]
          file1.writelines(L)
          file1.close()