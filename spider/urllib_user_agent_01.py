from urllib import request, error

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    try:
        #headers = {}
        #headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        #req = request.Request(url, headers=headers)
        req = request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
        print(req.headers)

        rsp = request.urlopen(req)
        html = rsp.read().decode()

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
    print('DONE..............')