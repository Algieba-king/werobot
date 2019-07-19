from urllib import request,parse
from http.cookiejar import CookieJar

# 使用cookiejar模擬登陸人人網

## 登陸

# 創建一個Cookiejar對象
cookiejar = CookieJar()
# 使用cookiejar對象創建一個HTTPCookieProcesor對象
handler = request.HTTPCookieProcessor(cookiejar)
# 使用opner發送登陸請求
opener = request.build_opener(handler)

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}
data = {
    'email':'9701380974@qq.com',
    'password':'pythonspider',
}

url = 'http://www.renren.com/PLogin.do'
req = request.Request(url=url,data=parse.urlencode(data).encode('utf-8'),headers=headers,method='POST')
opener.open(url)


## 訪問主頁

url = 'http://www.renren.com/443362311/profile'
# 獲取個人主頁的頁面時 由於此前的opener已然包含有所需信息 故此 直接用此前的opener
resp = opener.open(url)
html = resp.read().decode('utf-8')

with open('renren.html','w',encoding='utf-8') as f:
    f.write(html)
