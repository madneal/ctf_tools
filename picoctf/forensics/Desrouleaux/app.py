from pwn import remote

if __name__ == "__main__":
    r = remote('2018shell1.picoctf.com', 14079)
    print r.recvuntil("questions.") + "\n"
