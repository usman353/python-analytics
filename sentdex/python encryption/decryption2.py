from Crypto.Cipher import AES
import base64
import os


def decryption(encryptedString):
    padding = b'{'

    def DecodeAES(c, e): return c.decrypt(base64.b64decode(e)).rstrip(padding)
    key = b'\x16\x07#\xbc\x92V\xdc\xfb,i\xb1\xd5L\xa30\xd5'
    cipher = AES.new(key, AES.MODE_EAX)
    plaintext = cipher.decrypt(encryptedString)
    # decoded = DecodeAES(cipher, encryptedString)
    # print(decoded)
    print(plaintext)


decryption(b'/ieY4fDjS9gsesw+zKsPQUMvnFATstI9EskH9q60tQL80wW6BamoxVdlk0gkLBgD')
