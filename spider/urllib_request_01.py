from urllib import request

if __name__ == '__main__':
	url = "http://www.csdn.net"
	rsp = request.urlopen(url)
	html = rsp.read()
	print(type(html))
	html = html.decode('utf-8')
	print(html)