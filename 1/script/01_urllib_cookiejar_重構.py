from urllib import request,parse
from http.cookiejar import CookieJar

def get_Opener(url):
    # 鏈接數據預備
    url = 'http://www.renren.com/SysHome.do'
    data = {
        'email':'9701380974@qq.com',
        'password':'pythonspider'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    # 鏈接準備
    cookiejar = CookieJar()
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)

    # 模擬登陸獲取opener中的cookie
    opener.open(url)

    return opener

def login(url,filename,opener):
    url = 'http://www.renren.com/443362311/profile'
    resp = opener.open(url)
    html = resp.read().decode('utf-8')
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    opener = get_Opener(url='...')
    login(url='rrr',filename='renren.html',opener=opener)


