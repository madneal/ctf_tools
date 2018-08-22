import hashlib

if __name__ == '__main__':
    hash_str = "ac22543d5382cbf48b6ebcf6e40f123d9ca4b91f9998e4c2f2422402"
    salt = "zhangsanfeng"
    for i in range(1000000):
        if i < 1000000:
            i = '0' * (6 - len(str(i))) + str(i)
        if i == '877295':
            print(13)
        password = str(i + salt).encode('utf-8')
        print("Has tried password:")
        print(password)
        if hashlib.sha224(password).hexdigest() == hash_str:
            print("Found!!!")
            print("The flag is:")
            print("flag{{{}_sha224_{"
                  "}}}".format(i, salt))
            exit()
