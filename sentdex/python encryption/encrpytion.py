from Crypto.Cipher import AES
import base64
import os


def encryption(privateInfo):
    BLOCK_SIZE = 16
    PADDING = '{'

    def pad(s): return s + ((BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING).encode('utf-8')

    def EncodeAES(c, s): return base64.b64encode(c.encrypt(pad(s)))
    # secret = os.urandom(BLOCK_SIZE)
    secret = b'\x16\x07#\xbc\x92V\xdc\xfb,i\xb1\xd5L\xa30\xd5'
    print('encryption key : ', secret)
    cipher = AES.new(secret, AES.MODE_EAX)
    encoded = EncodeAES(cipher, privateInfo)
    print('encrypted string : ', encoded)


encryption(b"i am usman khan and want to learn ")
