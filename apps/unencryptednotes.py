aa = input("Are you going to open or create a file? (open/create):   ")

import apps.unencryptednotes
if aa == ('open'):
  a = input("Whats the title?   ")
  f = open((a) + ".txt", "r")
  notes = f.read()
  print (notes)
if aa == ('create'):
  a = input("Whats the title?   ")
  b = input("What do you want to write?   \n\n\n")
  f = open((a) + ".txt", "w")
  f.write(b)
  f.close()
import main
