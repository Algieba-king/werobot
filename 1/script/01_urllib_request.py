from urllib import request
from urllib import parse

url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%88%90%E9%83%BD&needAddtionalResult=false'

# resp = request.urlopen(url)
# print(str(resp.read()).encode('utf-8'))
# resp = parse.parse_qs(resp.read())
# print(resp)

data={
    'first': 'true',
    'pn': '1',
    'kd': '图像识别',
}
# data=parse.urlencode(data)
headers={
    'Referer': 'https://www.lagou.com/jobs/list_%E5%9B%BE%E5%83%8F%E8%AF%86%E5%88%AB?px=default&city=%E6%88%90%E9%83%BD',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
}
headers={
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8',
'Cache-Control': 'no-cache',
'Connection': 'keep-alive',
'Content-Length': '55',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'user_trace_token=20190718200911-806b0354-fdc4-4e7f-b54d-3bae83f65385; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563451749; _ga=GA1.2.1222277026.1563451749; LGUID=20190718200912-da8e4f64-a954-11e9-80cf-525400f775ce; JSESSIONID=ABAAABAAAIAACBIF49F2F91B8DACC1A22685E7F98738D23; _gid=GA1.2.1261383667.1563451763; index_location_city=%E5%85%A8%E5%9B%BD; X_MIDDLE_TOKEN=d8d0ca6a0921cce4b88e1e80398d8318; _gat=1; LGSID=20190719132603-b34f3366-a9e5-11e9-80fa-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c08b1d0100-097c3585674e59-3f385c06-1327104-16c08b1d0116f0%22%2C%22%24device_id%22%3A%2216c08b1d0100-097c3585674e59-3f385c06-1327104-16c08b1d0116f0%22%7D; sajssdk_2015_cross_new_user=1; ab_test_random_num=0; X_HTTP_TOKEN=c701e449a183f3ad6704153651e5d7d40eb688ec05; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563514073; LGRID=20190719132756-f6f523f1-a9e5-11e9-a4e9-5254005c3644; TG-TRACK-CODE=search_code; SEARCH_ID=fc46acd940044f42839f7da51146e8faukkjjjkkk',
'DNT': '1',
'Host': 'www.lagou.com',
'Origin': 'https://www.lagou.com',
'Pragma': 'no-cache',
'Referer': 'https://www.lagou.com/jobs/list_%E5%9B%BE%E5%83%8F%E8%AF%86%E5%88%AB?px=default&city=%E6%88%90%E9%83%BD',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
'X-Anit-Forge-Code': '0',
'X-Anit-Forge-Token': 'None',
'X-Requested-With': 'XMLHttpRequest',
}
req = request.Request(url=url,data=parse.urlencode(data).encode('utf-8'),headers=headers,method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
