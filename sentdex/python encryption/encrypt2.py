from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes, os
key = get_random_bytes(16)
print(key)


def encryption(data):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open("encrypted.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()


encryption('usman khanTypeError: Only byte strings can be passed to C code'.encode('utf-8'))
