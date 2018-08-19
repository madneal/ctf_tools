import gmpy2
import rsa

e = 65537
p = 302825536744096741518546212761194311477
q = 325045504186436346209877301320131277983
n = 98432079271513130981267919056149161631892822707167177858831841699521774310891

d = int(gmpy2.invert(e, (p - 1) * (q - 1)))
private_key = rsa.PrivateKey(n, e, d, p, q)

if __name__ == '__main__':
    filename = "/Users/neal/Downloads/fujian/encrypted.message1"
    filename2 = "/Users/neal/Downloads/fujian/encrypted.message2"
    filename3 = "/Users/neal/Downloads/fujian/encrypted.message3"
    with open(filename, 'rb') as f:
        print(rsa.decrypt(f.read(), private_key).decode())
    with open(filename2, 'rb') as f:
        print(rsa.decrypt(f.read(), private_key).decode())
    with open(filename3, 'rb') as f:
        print(rsa.decrypt(f.read(), private_key).decode())