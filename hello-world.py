# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
message = "The answer is nossdsfdafdasd"
ciphertext = obj.encrypt(message)

#print("".join("{0:x}".format(ord(e)) for e in ciphertext))

#ciphertext
#'\xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1'
obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')

#'The answer is no dfdfdfs'
#print(ciphertext)
#print(obj2.decrypt(ciphertext))

#print("Hello%s" % "Den")
import datetime
import json
#print(str(datetime.datetime.now()))

ans = {}
ans["e"] = "vgulaev@yandex.ru"
ans["t"] = "2013-12-17 04:51:37"
text_for_cipher = json.dumps(ans)
    
obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
ciphertext = obj.encrypt(text_for_cipher)

#forurl = "".join(e + ":" + "{0:02x}".format(ord(e)) + " ; " for e in ciphertext)
forurl = "".join("{0:02x}".format(ord(e)) for e in ciphertext)

print(text_for_cipher)
str = "f6a97746de7bdf60e918e57f44d72107cb7fc52de320431aa16c803fe238427ae73afb477ed11f23f5a206784e0faad1cba70f27ca67"
print(ciphertext)
print(obj2.decrypt(str.decode("hex")))

print(forurl)

#print(obj2.decrypt(ciphertext))
print("{0:02x}".format(99))