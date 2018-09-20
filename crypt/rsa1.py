import hashlib

if __name__ == '__main__':
    hash_str = "ac22543d5382cbf48b6ebcf6e40f123d9ca4b91f9998e4c2f2422402"
    salt = "zhangsanfeng"
    for i in range(1000000):
        if i < 1000000:
            print(i)
            password = '0' * (6 -len(str(i))) + str(i)
        else:
            password = str(i)
        password_ = str(password + salt).encode('utf-8')
        if hashlib.sha224(password_).hexdigest() == hash_str:
            print("Found")
            print("the flag is:" + password)
            exit()