import string


def compute(s):
    return (((ord(s) << 5) | (ord(s) >> 3)) ^ 111) & 255


def get_result(num, result):
    for s in str_arr:
        if compute(s) == num:
            print("the result is:" + s)
        else:
            continue


if __name__ == '__main__':
    verify_arr = [193, 35, 9, 33, 1, 9, 3, 33, 9, 225]
    result = ''
    str1 = string.ascii_letters
    str_arr = list(str1) + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for num in verify_arr:
        print("the num is: ")
        print(num)
        get_result(num, result)

