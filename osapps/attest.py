




from Crypto.Hash import SHA3_512

#Important modules to check: main.py, fileacess, settingsacces, attestation




a = open("main.py", "r")
mainsdd = a.read()
h_obj = SHA3_512.new()
h_obj.update(bytes(mainsdd, 'utf-8'))
hhbkvb = (h_obj.hexdigest())
if hhbkvb != "8eacd2da6f570225df48980fe8d529980195111a5ac31af01532d6776c761fc1136c9e9946f2327bb8b50c662e0652de44e7ae1663c13c3207d5adc075e9e78e":
  print ("The OS has been modified. Shutting down...")
  #exit()



#-----------------------------------------------
#once I figure out how to read files in foders I will add a function to verify encrypt apps and osapps
#@----------------------------------------------------
  







#if mode == ("hard"):
  #print ("verify with pgp")
  #pgp verification










import main
