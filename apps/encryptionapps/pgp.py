from Cryptodome.PublicKey import RSA
import os

print ("https://en.wikipedia.org/wiki/Pretty_Good_Privacy\n")
print ("Note- when inputting the name of a file, don't include the file type (ex: hello instead of hello.bin) \n")

wdjv = input("\nDo you want to \na) generate keys\nb) encrypt a message\nc) decrypt a message\n")


if wdjv == 'a':


  khblwpu = input ("What do you want your public key to be named?  ")
  khblwpr = input ("What do you want your private key to be named?  ")
  if khblwpu == khblwpr:
    print ("The two keys hve the same name, this will lead to error down the road. Terminating process")
    import main
    exit()
  kjutg = input("How long do you want your keys to be?\na) 2048\nb) 4096\n")
  if kjutg == 'a':
    hgcv = 2048
  if kjutg == 'b':
    hgcv = 4096

  key = RSA.generate(hgcv)
  private_key = key.export_key()
  file_out = open("trxctycjtfcxjycjycrjgtfxrderswa.pem", "wb")
  file_out.write(private_key)
  file_out.close()

  public_key = key.publickey().export_key()
  file_out = open("jyfrxgrwqawzsvlgyjfcjyfrxyreyre.pem", "wb")
  file_out.write(public_key)
  file_out.close()

  print ("Keys generated!\n\n")

  os.rename('trxctycjtfcxjycjycrjgtfxrderswa.pem', (khblwpr) + '.pem')
  os.rename('jyfrxgrwqawzsvlgyjfcjyfrxyreyre.pem', (khblwpu) + '.pem')

  print ("Public key saved as   ", (khblwpu) + ".pem")
  print ("Private key saved as   ", (khblwpr) + ".pem")



  import main 



if wdjv == 'b':
  from Cryptodome.PublicKey import RSA
  from Cryptodome.Random import get_random_bytes
  from Cryptodome.Cipher import AES, PKCS1_OAEP
  jhbjbh = input("What do you want the file to be saved as?   ")
  jgvsss = input("What do you want to encrypt?    ")
  data = (jgvsss).encode("utf-8")
  file_out = open("encrypted_data.bin", "wb")

  wesd = input("What's the public key called?   ")
  recipient_key = RSA.import_key(open((wesd) + ".pem").read())
  session_key = get_random_bytes(16) #Add key name for encrypted and decrypting

  # Encrypt the session key with the public RSA key
  cipher_rsa = PKCS1_OAEP.new(recipient_key)
  enc_session_key = cipher_rsa.encrypt(session_key)

  # Encrypt the data with the AES session key
  cipher_aes = AES.new(session_key, AES.MODE_EAX)
  ciphertext, tag = cipher_aes.encrypt_and_digest(data)
  [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
  file_out.close()

  os.rename('encrypted_data.bin', (jhbjbh) + '.bin')
  print ("Encrypted text saved as", (jhbjbh))

  import main



if wdjv == 'c':
  from Cryptodome.PublicKey import RSA
  from Cryptodome.Cipher import AES, PKCS1_OAEP

  tyvutu = input("What is the file that has the encrypted message named?   ")
  file_in = open((tyvutu) + ".bin", "rb")

  wesdd = input("What's the private key called?   ")
  private_key = RSA.import_key(open((wesdd) + ".pem").read())

  enc_session_key, nonce, tag, ciphertext = \
    [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

  # Decrypt the session key with the private RSA key
  cipher_rsa = PKCS1_OAEP.new(private_key)
  session_key = cipher_rsa.decrypt(enc_session_key)

  print (" ")
  # Decrypt the data with the AES session key
  cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
  data = cipher_aes.decrypt_and_verify(ciphertext, tag)
  print(data.decode("utf-8"))

  import main



