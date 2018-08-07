import hashlib



if __name__ == '__main__':
    hash_str = "ac22543d5382cbf48b6ebcf6e40f123d9ca4b91f9998e4c2f2422402"
    salt = "zhangsanfeng"
    filename = "superdic.txt"
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for password in data:
            password = password.replace("\n", "")
            pass_ = str(password + salt).encode('utf-8')
            if hash_str in hashlib.sha1(pass_).hexdigest() is True:
                print(password)
                exit()
            # elif hash_str in hashlib.sha256(pass_).hexdigest()is True:
            #     print(password)
            #     exit()
            elif hashlib.sha224(pass_).hexdigest() == hash_str:
                print('sha224')
                print(password)
                exit()
            elif hashlib.sha512(pass_).hexdigest() == hash_str:
                print('sha512')
                print(password)
                exit()
            elif hashlib.sha384(pass_).hexdigest() == hash_str:
                print('sha384')
                print(password)
                exit()
            elif hashlib.sha3_224(pass_).hexdigest() == hash_str:
                print('sha3_224')
                print(password)
                exit()
            elif hashlib.sha3_256(pass_).hexdigest() == hash_str:
                print('sha3_256')
                print(password)
                exit()
            elif hashlib.sha3_384(pass_).hexdigest() == hash_str:
                print('sha3_384')
                print(password)
                exit()
            elif hashlib.sha3_512(pass_).hexdigest() == hash_str:
                print('sha3_512')
                print(password)
                exit()
            else:
                print("has tried password " + password)
                continue

