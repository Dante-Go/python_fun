from urllib import request
from bs4 import BeautifulSoup
import re

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

#content = soup.prettify()
#print(content)
print('==' * 12)
tags = soup.find_all(re.compile('^me'), content='always')
for tag in tags:
    print(tag)
print('==' * 12)
#nodes = soup.contents
#print(nodes)

#childrenNodes = soup.children
#for node in childrenNodes:
#    print(node)

