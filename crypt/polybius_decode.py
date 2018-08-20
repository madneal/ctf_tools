if __name__ == '__main__':
    str = "3534315412244543_434145114215_132435231542"
    dict = {
        "11": "A",
        "12": "B",
        "13": "C",
        "14": "D",
        "15": "E",
        "21": "F",
        "22": "G",
        "23": "H",
        "24": "I/J",
        "25": "K",
        "31": "L",
        "32": "M",
        "33": "N",
        "34": "O",
        "35": "P",
        "41": "Q",
        "42": "R",
        "43": "S",
        "44": "T",
        "45": "U",
        "51": "V",
        "52": "W",
        "53": "X",
        "54": "Y",
        "55": "Z",
    }
    cnt = 0
    key = ""
    result = ""
    tmp = ""
    for s in str:
        if cnt < 2:
            cnt = cnt + 1
            key += s
        elif not s.isdigit():
            tmp = s
        else:
            result += dict[key]
            if cnt % 2 == 0:
                result += tmp
                tmp = ""
            key = s
            cnt = 1
    result += dict[str[len(str) - 2:len(str) - 0]]
    print("the result is:")
    print(result.lower())
