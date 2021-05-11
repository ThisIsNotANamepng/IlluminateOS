from hashlib import sha256
from hashlib import sha1
from hashlib import sha512
from hashlib import md5
from hashlib import sha384
from hashlib import blake2b
from hashlib import blake2s
from hashlib import sha3_224
from hashlib import sha3_384

#from Crypto.Hash import MD2
#from Crypto.Hash import keccak
#from Crypto.Hash import RIPEMD160
print ("https://en.wikipedia.org/wiki/Cryptographic_hash_function\n")
hashthis = input("What do you want to hash?   ")



print (' ')
print ("MD5")
h = md5()
h.update(bytes(hashthis, 'utf-8'))
hash = h.hexdigest()
print(hash)

print (" ")
print ("SHA1")
h = sha1()
h.update(bytes(hashthis, 'utf-8'))
hash = h.hexdigest()
print(hash)

print (' ')
print ("SHA224")
h = sha3_224()
h.update(bytes(hashthis, 'utf-8'))
hash = h.hexdigest()
print(hash)

print (" ")
print ("SHA256")
h = sha256()
h.update(bytes(hashthis, 'utf-8'))
hash = h.hexdigest()
print(hash)

print (' ')
print ("Blake2s")
h = blake2s()
h.update(bytes(hashthis, 'utf-8'))
hash = h.hexdigest()
print(hash)

print (' ')
print ("SHA384")
h = sha3_384()
h.update(bytes(hashthis, 'utf-8'))
hash = h.hexdigest()
print(hash)

print (' ')
print ("Blake2b")
h = blake2b()
h.update(bytes(hashthis, 'utf-8'))
hash = h.hexdigest()
print(hash)

print (' ')
print ("SHA512")
h = sha512()
h.update(bytes(hashthis, 'utf-8'))
hash = h.hexdigest()
print(hash)

import main
