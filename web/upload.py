import base64
import requests
import hashlib


def get_path():
    s = requests.session()
    r = s.get("http://1e08345357de47889a358c8d513c2a5d6bd5b9bdd63b4028.game.ichunqiu.com/")
    key = r.headers["flag"]
    base64_key = base64.b64decode(key)
    arr = str(base64_key).split(":")
    key = base64.b64decode(arr[1])
    body = {
        "ichunqiu": key
    }
    res = s.post("http://1e08345357de47889a358c8d513c2a5d6bd5b9bdd63b4028.game.ichunqiu.com/", data=body)
    return res.text


def md5(s):
    return hashlib.md5(str(s).encode('utf-8')).hexdigest()


def get_captcha(s):
    for i in range(1, 99999999):
        if md5(i)[0:6] == str(s):
            print(i)
            exit()


if __name__ == '__main__':
    get_captcha("d76364")