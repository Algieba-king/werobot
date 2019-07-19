from urllib import request
from urllib import parse

#parse （語法）庫文件 處理編碼

#
parameter = {'username':'root','nickname':'謎之聲','password':'SomIsU'} #傳入參數為字典
# parameter = "\'\"and 1=1" # 測試發現 不能講字符串進行編碼
print("Original parameter:"+str(parameter))
parameter = parse.urlencode(parameter)
print("Encoded parameter :"+parameter)
# username=root&nickname=%E8%AC%8E%E4%B9%8B%E8%81%B2&password=SomIsU
# 會自動解析成url用的形式

parameter = parse.parse_qs(parameter)
print(parameter)

