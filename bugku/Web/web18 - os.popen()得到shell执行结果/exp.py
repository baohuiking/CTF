import re
import requests
import os
session = requests.Session()

url = 'http://114.67.246.176:12628/'
cookies = {
    'PHPSESSID': 'i6qvcr067dve40nrmavoevjo05'
}
res = session.get(url=url, cookies=cookies)

nums_s = re.findall(r'<div>.*?</div>', res.text)[0].replace('<div>', '').replace('=?;</div>', '')   # 获取算式

# os.popen()可以获得系统shell执行后的结果
result = os.popen('python -c print(' + nums_s + ')')
sum = result.read() 
sum = int(str(sum), 10)

data = {
    'value': sum
}

res2 = session.post(url=url, data=data, cookies=cookies)

print(res2.content)