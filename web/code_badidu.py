import requests
import string
from base64 import *


if __name__ == '__main__':
    url = "http://089d756e9073405d8ef3353fffd2153bb1f150d374c646a8.game.ichunqiu.com/fl3g_ichuqiu.php"
    cookie = requests.get(url).cookies['user']
    txt = b64decode(cookie)
    rnd = txt[:4]
    ttmp = txt[4:]
    keys = list("xxxxxx")
    guest = list("guest")

    for i in range(len(guest)):
        guest[i] = chr(ord(guest[i]) + 10)
    for i in range(len(guest)):
        keys[i] = chr(ord(chr(ttmp[i])) ^ ord(guest[i]))

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
        print(b64decode(str))
        ttmp_new = ""