from urllib import request, error
import chardet

if __name__ == '__main__':
    url = 'http://www.sipo.gov.cn/'

    proxy = {'http': '158.140.172.162:8080'}
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
        html = rsp.read()
        cs = chardet.detect(html)
        html = html.decode(cs.get('encoding', 'utf-8'))
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)