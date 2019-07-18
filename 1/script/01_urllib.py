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
url='https://www.lgstatic.com/i/image2/M01/62/3C/CgotOV0tROeANdp4AACKU68GAEc723.JPG'
request.urlretrieve(url=url,filename='lagou.jpg')