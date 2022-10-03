import os 
def UpdateExtentions():
          dir_path = "/downloads/"
          res = []
          for file in os.listdir(dir_path):
                    if file.endswith('.mp4'):
                              res.append(file)
                              print(res)