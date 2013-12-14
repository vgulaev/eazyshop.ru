# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is no"
ciphertext = obj.encrypt(message)

print("".join("{0:x}".format(ord(e)) for e in ciphertext))

#ciphertext
#'\xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1'
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')

#'The answer is no'
print(ciphertext)
print(obj2.decrypt(ciphertext))