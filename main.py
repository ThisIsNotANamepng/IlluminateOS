print ("Booting up IlluminateOS...")

from termcolor import colored, cprint
from Crypto.Hash import SHA3_512
import replit
import os



import osapps.attestation


def clear():
  os.system('clear') 

  
def calculator():
  import apps.calculator
          
def encryptos():
  print ("Encrypt the OS")
  cprint ("This action will render the entire OS unuseable if you forget the password. Do not use it lightly", 'red')
  print ("This feature is still a work in progress")
  mainmenu()



def unencryptednotes():
  import apps.unencryptednotes

def encryptednotes():
  import apps.encryptednotes

def changelockscreenpassword():
  cprint ("Changing lock screen password", 'green')
  qaqaqa = input("What's the current password?   ")


  h_obj = SHA3_512.new()

  h_obj.update(bytes(qaqaqa, 'utf-8'))

  kutck = (h_obj.hexdigest())

  g = open('codes.txt', 'r')
  gg = g.read()
  if gg != kutck:
    print ('Frick you, go away')
    g.close()
    exit()

  if gg == kutck:
    newpassword = input("What do you want the new password to be?   ")
    newpassword2 = input("Please type the new password again         ")
    h_obj = SHA3_512.new()
    h_obj.update(bytes(newpassword, 'utf-8'))
    nphash = (h_obj.hexdigest())

    h_obj = SHA3_512.new()
    h_obj.update(bytes(newpassword2, 'utf-8'))
    np2hash = (h_obj.hexdigest())
    
    if nphash != np2hash:
      print ("The two passwords are not the same")
      changelockscreenpassword()

    if nphash == np2hash:
      print ("The two passwords are the same")
      g = open('codes.txt', 'w')
      g.write(nphash)
      g.close()
      mainmenu()
    g.close()    
    mainmenu()

  

headcolor = ('yellow')

def settings():
  cprint ("Settings", (headcolor))
  choosesettings = input("a) Encrypt OS\nb) Change Lock Screen Password\n")
  if choosesettings == 'a':
    encryptos()
  if choosesettings == 'b':
    changelockscreenpassword()

  mainmenu()



def information():
  print ("\n")
  print ("This is a rudementary os-type thing. It has preinstalled apps created by me. Most of them are privacy-security related, as that's what I'm into and what I have the most experience coding, but I will totally add other apps that other people write. Until I create a file and permission system, I won't be adding an official option to add apps. Enjoy! ")
  cprint ("Information", (headcolor))
  cwd = os.getcwd() 
  print("Current working directory:", cwd) 
  print(os.name)
  tyesxc = input("\nDo you want information about the different apps included in the os?  (y/n)   ")

  if tyesxc == 'y':
    print ("\npgp - https://en.wikipedia.org/wiki/Pretty_Good_Privacy")
    print ("\nencryption - https://en.wikipedia.org/wiki/Encryption")
    print ("\npython - https://en.wikipedia.org/wiki/Python_(programming_language)")
    print ("\nhashing - https://en.wikipedia.org/wiki/Cryptographic_hash_function")
    print ("\nverified boot - https://source.android.com/security/verifiedboot")
    print ("\nos - https://en.wikipedia.org/wiki/Operating_system")
    mainmenu()


  if tyesxc == 'n':
    mainmenu()
  

def firefox():
  import apps.firefox
 


cprint ("Welcome to IlluminateOS", 'green')

def mainmenu():
  cprint ("Menu", (headcolor))
  menu = input("\na) Apps\nb) Information\nc) Settings\n")
  if menu == 'a':
    appmenu()
  if menu == 'b':
    information()
  if menu == 'c':
    settings()


def appmenu():
  cprint ("\nApps", (headcolor))
  chooseapp = input("a) Firefox\nb) calculator\nc) notes\nd) Encrypted Notes\ne) Files *Not working*\nf) Back to main menu\ng) Encryption apps\nh) Validate apps and os\ni) Google Search\n")
  if chooseapp == ('a'):
    firefox()
  if chooseapp == ("b"):
    calculator()
  if chooseapp == ('f'):
    mainmenu()
  if chooseapp == ('d'):
    encryptednotes()
  if chooseapp == ('c'):
    unencryptednotes()
  if chooseapp == ('e'):
    import fileacess
  if chooseapp == ('g'):
    chenap = input("\na) Hashing\nb) File Checksum\nc) PGP\nd) Text Encryption\n")
    if chenap == ('a'):
      import apps.encryptionapps.hashing
    if chenap == ('b'):
      import apps.encryptionapps.filecheck
    if chenap == ('c'):
      import apps.encryptionapps.pgp
    if chenap == ('d'):
      import apps.encryptionapps.textenc
  if chooseapp == ('h'):
    import osapps.attest
  if chooseapp == ('i'):
    import apps.search





#cprint("Hello", 'red')
#print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')

#for i in range(10):
#    cprint(i, 'magenta', end=' ')

#cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)


def lockscreen():
  cprint ("Lock Screen", 'red')
  print ("The password is 'm' for now, you can change it later")

  ewvwv = input("What's the password?   ")

  h_obj = SHA3_512.new()

  h_obj.update(bytes(ewvwv, 'utf-8'))

  kutck = (h_obj.hexdigest())

  g = open('codes.txt', 'r')
  gg = g.read()
  if gg != kutck:
    print ('Frick you, go away')
    g.close()
    exit()

  if gg == kutck:
    print ("Password correct")
    g.close()
    os.system('clear') 
    mainmenu()








lockscreen()
