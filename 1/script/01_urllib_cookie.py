#encoding:utf-8
from urllib import request
from urllib import parse

qq_zone = 'https://user.qzone.qq.com/960033850/infocenter'

#不使用cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
}

req = request.Request(url=qq_zone,headers=headers,method='GET')
resp = request.urlopen(req)
# request.urlretrieve(req,'qq_0cookie.html')
print(resp.read().decode('utf-8')) #這個讀取只能讀一次 這裡讀過一次之後 resp.read()就沒有內容了 以致于後面保存均為空白
html = resp.read().decode('utf-8')
print('^^^^^^^^'+html+'\n^^^^^^^^^^^^^^^^^^')
with open('qq_cookie.html','w',encoding='utf-8') as f:
    #由於Windows環境下 新的文件默認編碼為gbk 故需要指定編碼才能進行有效存儲
    f.write(html)

