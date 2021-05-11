




from Crypto.Hash import SHA3_512

#Important modules to check: main.py, fileacess, settingsacces, attestation




a = open("main.py", "r")
mainsdd = a.read()
h_obj = SHA3_512.new()
h_obj.update(bytes(mainsdd, 'utf-8'))
hhbkvb = (h_obj.hexdigest())
if hhbkvb != "ffe3ed5fbada9b8c12efe51270d2688c2d0a2715549941efb752e27995f104599563e734dd14532b1e7b47cf23a46f10c890dc1f3d900356f5553e37649b1b60":
  print ("The OS has been modified. Shutting down...")
  print (hhbkvb)
  #exit()
if hhbkvb == 'ffe3ed5fbada9b8c12efe51270d2688c2d0a2715549941efb752e27995f104599563e734dd14532b1e7b47cf23a46f10c890dc1f3d900356f5553e37649b1b60':
  print ("The OS is validated\n")



#-----------------------------------------------
#once I figure out how to read files in foders I will add a function to verify encrypt apps and osapps
#@----------------------------------------------------
  







#if mode == ("hard"):
  #print ("verify with pgp")
  #pgp verification










import main
