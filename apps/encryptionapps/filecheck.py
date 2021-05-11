# Python rogram to find the SHA-1 message digest of a file

# importing the hashlib module

import hashlib
print ("https://en.wikipedia.org/wiki/File_verification#Authenticity_verification\n")

name = input("What's the file that you want to hash? (The file can't be in a folder, include the file type in the name)\n\nFor example, you could ask README.md\n\n")


def hash_file(filename):
   """"This function returns the SHA-512 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha512()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

def hash_filee(filename):
   """"This function returns the SHA-512 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha256()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

def hash_fileee(filename):
   """"This function returns the SHA-512 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

def hash_fileeee(filename):
   """"This function returns the SHA-512 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.md5()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()





message = hash_file(name)
messagee = hash_filee(name)
messageee = hash_fileee(name)
messageeee = hash_fileeee(name)
print ("\nSHA-512")
print(message, "\n")
print ("SHA-256")
print (messagee, "\n")
print ("Sha-1")
print (messageee, "\n")
print ("md5")
print (messageeee, "\n")


import main
