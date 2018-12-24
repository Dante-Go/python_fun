import requests
import json

baseUrl = 'https://fanyi.baidu.com/sug'

data = {
	'kw': 'fury'
}
headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
	'Content-Length': str(len(data))
}

#rsp = requests.post(baseUrl, data=data, headers=headers, verify=False)
rsp = requests.post(baseUrl, data=data, headers=headers)

print(rsp.text)
print(rsp.json())
