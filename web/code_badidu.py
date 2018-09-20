import requests
import string
from base64 import *


if __name__ == '__main__':
    url = "http://4341318268e2438285a76b4e38fa930f185d4cd2989443c0.game.ichunqiu.com/fl3g_ichuqiu.php"
    cookie = requests.get(url).cookies['user']
    txt = b64decode(cookie)
    rnd = txt[:4]
    ttmp = txt[4:]
    keys = list("xxxxxx")
    guest = list("guest")

    for i in range(len(guest)):
        print(guest[i])
        print(ord(guest[i]) + 10)
        guest[i] = chr(ord(guest[i]) + 10)
        print(guest[i])
    for i in range(len(guest)):
        keys[i] = chr(ord(ttmp[i]) ^ ord(guest[i]))

    system = list("system")

    for i in range(len(system)):
        system[i] = chr(ord(system[i]) + 10)

    ttmp_new = ""
    str = ""
    letters = "1234567890abcdef"
    for ch in letters:
        keys[5] = ch
        for i in range(len(system)):
            ttmp_new += chr(ord(keys[i]) ^ ord(system[i]))
        str = rnd + ttmp_new
        print(b64decode(str).decode('utf-8'))
        ttmp_new = ""