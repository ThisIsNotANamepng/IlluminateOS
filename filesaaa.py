print ("You have reached the files librarian")


from fileacess import fileaccess
print (fileaccess)


if fileaccess == 0:
  print ("System error. Return to the main menu")
  mainmenu()
if fileaccess == 2:
  print("You are here ilegally. System shutting down")
  exit()
if fileaccess == 1:
  print ("Access granted. Continue")


















