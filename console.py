from os import system, name


def Clear():
   if name == 'nt':
      _ = system('cls')
   else:
           _ = system('clear')