import wave
import struct
from scipy import *
from pylab import *

if __name__ == '__main__':
    # 读取wav文件，我这儿读了个自己用python写的音阶的wav
    filename = 'music.wav'
    wavefile = wave.open(filename, 'r')  # open for writing

    # 读取wav文件的四种信息的函数。期中numframes表示一共读取了几个frames，在后面要用到滴。
    nchannels = wavefile.getnchannels()
    sample_width = wavefile.getsampwidth()
    framerate = wavefile.getframerate()
    numframes = wavefile.getnframes()

    print("channel", nchannels)
    print("sample_width", sample_width)
    print("framerate", framerate)
    print("numframes", numframes)

    # 建一个y的数列，用来保存后面读的每个frame的amplitude。
    y = zeros(numframes)
    result = []
    result1 = ''
    count = 1
    tmp = ''
    data = []
    result2 = ''
    for i in range(numframes):
        val = wavefile.readframes(1)
        # print(struct.unpack('h', val))[0]
        left = val[0:2]
        # right = val[2:4]
        v = struct.unpack('h', left)[0]
        y[i] = v
        data.append(v)
    count = 1
    aaa = ""
    for index, ele in enumerate(data):
        aaa += ";" + str(ele)
        index = index + 1
        if index % 12 == 0:
            print(aaa)
            print("\n")
            aaa = ""
        if index % 12 == 3:
            # print(ele)
            if ele > 20000:
                # print(str(ele) + '==>1')
                result2 = result2 + '1'
            else:
                # print(str(ele) + '==>0')
                result2 = result2 + '0'
        # if i < count * 12:
        #     if v > 16385:
        #         tmp += '1'
        #     else:
        #         tmp += '0'
        # else:
        #     # print("the tmp is:" + tmp)
        #     # print("the index is:" + str(i))
        #     result.append(tmp)
        #     if v > 16385:
        #         tmp = '1'
        #     else:
        #         tmp = '0'
        #     count = count + 1

    for ele in result:
        # print(len(ele))
        # print(ele)
        result1 += ele[5]

    # print(result1)
    # print("result2:")
    print(result2)

    # framerate就是44100，文件初读取的值。然后本程序最关键的一步！specgram！实在太简单了。。。

