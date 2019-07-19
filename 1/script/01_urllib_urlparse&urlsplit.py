from urllib import parse

url='https://robottest.ro/cloud/image/s.jsp;key;key1?id=1&pw=2&flag=0#3'

url0=parse.urlsplit(url)
url1=parse.urlparse(url)
print(url1)