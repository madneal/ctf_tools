#!/usr/bin/env python3

import os
import sys

class XOR_CBC:
    BLOCK_SIZE = 16

    def __init__(self, key: bytes, iv: bytes):
        self.key = key
        self.iv = iv
        assert len(key) == len(iv) == self.__class__.BLOCK_SIZE

    def pad(self, msg: bytes):
        l = len(msg)
        padding_len = 16 - len(msg) % 16
        return msg + (chr(padding_len) * padding_len).encode()

    def xor(self, a, b):
        return bytes([x ^ b[i%len(b)] for i, x in enumerate(a)])

    def encrypt(self, msg: bytes):
        padded_msg = self.pad(msg)

        block_size = self.__class__.BLOCK_SIZE

        assert len(padded_msg) % block_size == 0
        count = len(padded_msg) // block_size

        c = []

        last = self.iv
        for i in range(count):
            xored_plain = self.xor(padded_msg[i*block_size:(i+1)*block_size], last)
            cipher_text = self.xor(xored_plain, self.key)
            last = cipher_text
            c.append(cipher_text)

        return b''.join(c)

def decrypt(str):
        c_arr = str.split('')
        print(c_arr)


def decode(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    print(data)
    # arr = str(data)
    # print(arr)
    return data


if __name__ == '__main__':
    data = decode("plain.txt.encrypted")
    for ele in data:
        print(ele)

    # if len(sys.argv) < 2:
    #     print('usage: %s <plain_text>')
    #     sys.exit(0)
    #
    # key = os.urandom(16)
    # iv = os.urandom(16)
    # cipher = XOR_CBC(key, iv)
    # encrypted = cipher.encrypt(b"Please make sure keep this secret safe.")
    # print(encrypted)

    # with open(sys.argv[1], 'rb') as f:
    #     encrypted = cipher.encrypt(f.read())
    #
    # with open(sys.argv[1]+'.encrypted', 'wb') as f:
    #     f.write(encrypted)

