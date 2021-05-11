aa = input("Are you going to open or create a file? (open/create):   ")
import cryptocode
from Crypto.Hash import SHA3_512


if aa == ('open'):
  a = input("Whats the title?   ")
  b = input("What's the password?   ")
  obj = SHA3_512.new()
  obj.update(bytes((a), encoding='utf-8'))
  e = (obj.hexdigest())
  f = open((e) + ".txt", "r")
  encoded = f.read()
  decoded = cryptocode.decrypt(encoded, (b))
  print (decoded)

if aa == ('create'):
  a = input("Whats the title?   ")
  b = input("What do you want to write?   \n\n\n")
  c = input("What do you want your password to be?   ")
  obj = SHA3_512.new()
  obj.update(bytes((a), encoding='utf-8'))
  e = (obj.hexdigest())
  encoded = cryptocode.encrypt((b),(c))
  f = open((e) + ".txt", "w")
  f.write(encoded)
  f.close()
  print (encoded)





import main
mainmenu()