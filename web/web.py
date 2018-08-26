from hashlib import *


def md5_decode():
    str = "ichunqiu"
    result = "1b4167610ba3f2ac426a68488dbd89be"
    str_list = "abcdefghijklmnopqrstuvwxyz0123456789"
    for a in str_list:
        for b in str_list:
            for c in str_list:
                key = (str + a + b + c).encode('utf-8')
                # print("has tried:" + key)
                hashed_str = md5(key).hexdigest()
                print("has tried:" + str + a + b + c)
                if hashed_str == result:
                    print("found")
                    print(key)
                    exit(-1)
                else:
                    continue


if __name__ == '__main__':
    md5_decode()