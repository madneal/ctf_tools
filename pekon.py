

if __name__ == '__main__':
    a = []
    b = []
    dic = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb',
           'E': 'aabaa', 'F': 'aabab', 'G': 'aabba', 'H': 'aabbb',
           'I': 'abaaa', 'J': 'abaab', 'K': 'ababa', 'L': 'ababb',
           'M': 'abbaa', 'N': 'abbab', 'O': 'abbba', 'P': 'abbbb',
           'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
           'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb',
           'Y': 'bbaaa', 'Z': 'bbaab'
    }
    peigen = 'woUld you prEfeR SausaGes or bacoN wiTH YouR EgG'
    print('培根密码的密文为：')
    print(peigen)
    pgs = list(peigen.replace(' ', ''))
    for pg in pgs:
        if pg.isupper():
            a.append('b')
    else:
        a.append('a')
    i = 1
    j = 5
    for i in range(1, len(a) // 5 + 1):
        c = ''.join(a[j * i - 5:j * i])
    b.append(c)
    print('翻译为:')
    di = {}
    for password in b:
        if password in dic.values():
            di = {v: k for k, v in dic.items()}
            print(di[password])