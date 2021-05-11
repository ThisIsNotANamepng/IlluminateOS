print ("https://en.wikipedia.org/wiki/Encryption\n")

print ("This tool will encrypt your text with the cryptocode library. This libary hasn't ever been updated and it's not well known at all, but it works. DO NOT use it for sensitive communication\n\nIf it doesen't work, type 'pip install cryptocode' into the shell\n")


import cryptocode


enc = input("What do you want to encrypt?   ")
pwd = input("What's the password?   \n")



myEncryptedMessage = cryptocode.encrypt((enc), (pwd))




print(myEncryptedMessage)


import main
mainmenu()
