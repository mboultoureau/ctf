#!/usr/bin/python3
from Crypto.Cipher import AES
import base64
import re


msg = "62C7B5577F886374780C354DA7D9655EE2C1A9F2752C6BC395D256744BAA9C4C"
key = "CA56375A73BBE3ECCD7E8A64F55A41B7"

key = bytes.fromhex(key)
message = bytes.fromhex(msg)

for i in range(0, 1000):
    cipher = AES.new(key, AES.MODE_ECB)
    message = cipher.decrypt(message)

print(re.search("(ENSIBS{[A-Za-z0-9_-]+})", message.decode("utf-8")).group(1))