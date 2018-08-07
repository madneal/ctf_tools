import base64
import string

def encode(message):
    s = ''
    for i in message:
        x = ord(i) ^ 32
        x = x + 16
        s += chr(x)

    return base64.b64encode(s)

def encode_s(i):
    s = ""
    x = ord(i) ^ 32
    x = x + 16
    s += chr(x)


def decode(message):
    result = ""
    for s in message:
        for c in string.printable:
            if encode_s(c) == s:
                result = result + c
    return result


if __name__ == '__main__':
    correct = 'XlNkVmtUI1MgXWBZXCFeKY+AaXNt'
    flag = ""
    msg = base64.b64decode(correct)
    msg = list(msg)
    for i in msg:
        i = chr((i - 16) ^ 32)
        flag += i
    print(flag)

