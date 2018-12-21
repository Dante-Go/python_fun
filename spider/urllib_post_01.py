from urllib import request, parse
import json

base_url = 'https://fanyi.baidu.com/sug'

kw = input('input the word:')
data = {
    'kw': kw
}
data = parse.urlencode(data).encode('utf-8')
print(type(data))

headers = {
    'Conent-Length': len(data)
}

rsp = request.urlopen(base_url, data=data)

json_data = rsp.read().decode('utf-8')
print(type(json_data))
print(json_data)

json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'], "--", item['v'])