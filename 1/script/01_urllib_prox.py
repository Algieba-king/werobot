from urllib import request

url = 'http://httpbin.org/ip'
# url = 'http://www.ip138.com'
# 無代理
# resp = request.urlopen(url)
# print(resp.read()) #b'{\n  "origin": "117.173.131.189, 117.173.131.189"\n}\n'

# 使用代理

# 1.使用ProxyHandler 傳入代理，構建hanlder
handler = request.ProxyHandler({'http':'118.24.172.37:1080'})
# 2. 使用構建的handler構建一個opener
opener = request.build_opener(handler)
# 3. 使用opener發送請求
resp = opener.open(url)
print(resp.read())

handler = request.ProxyHandler({'http':'187.53.61.50:80'})
opener = request.build_opener(handler)
resp = opener.open(url)
print(resp.read())