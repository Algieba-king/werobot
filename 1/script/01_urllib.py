from urllib import  request

# response = request.urlopen('www.taobao.com') # 不能打開 因為沒有加http
url = 'http://www.baidu.com'
# url = 'http://taobao.com' #淘寶做了反爬？
response = request.urlopen(url=url)
web_status = response.status
web_read = response.read()
web_read_line=response.readline()
# print(web_read_line+b'\n')
# print(web_read)
# print(type(response)+'\n')
# print(response.status)

request.urlretrieve(url=url,filename='baidu.html')