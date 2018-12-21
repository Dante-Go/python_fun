from urllib import request
import chardet
from urllib import parse

if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'
    wd = input("Input your keyword:")

    qs = {
        "wd": wd
    }
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    rsp = request.urlopen(fullurl)
    html = rsp.read()
    cs = chardet.detect(html)
    html = html.decode(cs.get('encoding', 'utf-8'))
    print(html)
    # print('URL: {0}'.format( rsp.geturl()))
    # print('Info: {0}'.format( rsp.info()))
    # print('Code: {0}'.format( rsp.getcode()))

