


author = ""
def Reader():
          var="god knows what"
          
         
with open('list.txt') as f:
    for line in f:
          if line.find(':')>0:
                    author = line
                    print(line)
          else:
                    print(author.replace(':','')+" "+line+" letra")
                    
Reader()