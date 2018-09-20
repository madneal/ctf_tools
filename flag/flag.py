

if __name__ == '__main__':
    with open('flag.jpg', 'rb') as f:
        data = f.read()
        print(data[0])
        print(data[len(data)])
        data = list(data)
        data_ = data.reverse()
        print(data[0])
        print(data_.decode('utf-8', errors='ignore'))