# 参考资料
- python网络数据采集
- 精通Python爬虫框架Scrapy
- Python3网络爬虫
- Scrapy官方教程

# 爬虫
## 前置知识
- url
- http协议
- web前端，html，css，js
- ajax
- re，xpath
- xml
## 别名
- 蚂蚁、自动索引、模拟程序或蠕虫
## 两大特征
- 能按作者要求下载数据或者内容
- 能自动在网络上漫游
## 三大步骤
- 下载网页
- 提取正确的信息
- 根据一定规则自动跳到另外的网页上执行前两步
## Python网络包简介
- Python2.x: urllib, urllib2, urllib3, httplib, httplib2, requests
- Python3.x: urllib, urllib3, httplib2, requests

# urllib
## 包含模块
- urllib.request: 打开和读取urls
- urllib.error: 包含urllib.request产生的常见错误，使用try捕捉
- urllib.parse: 包含解析url的方法
- urllib.robotparse: 解析robots.txt文件
## 网页编码问题
- chardet可以自动检测页面文件的编码格式，但是，可能有误
- 需要安装: conda install chardet
## url的返回对象
- geturl: 返回请求对象的url
- info: 请求反馈对象的meta信息
- getcode：返回的http code
## request.data的使用
- 访问网络的两种方法
    - get:
        - 利用参数给服务器传递信息
        - 参数为dict，然后用parse编码
    - post
        - 一般向服务器传递参数使用
        - post把信息自动加密处理
        - 使用post，需要http请求头可能需要更改：
            - Content-Type : application/x-www-form-urlencode
            - Content-Length : 数据长度
        - urllib.parse.urlencode
        - 为了更多的设置请求信息，单纯的通过urlopen函数已经不大好用了，需要使用request.Request类
## urllib.error
- URLError产生的原因：
    - 网络状况差
    - 服务器链接失败
    - DNS无法解析出服务器地址
    - OSError的子类
- HTTPError
    - URLError的子类
- HTTPError和URLError
    - HTTPError是对应的HTTP请求的返回码错误，如果返回400以上，则引发HTTPError
    - URLError对应的一般是网络问题，包括url问题
## UserAgent
- UserAgent：属于head的一部分，服务器通过UA来判断访问者身份
- 常见的UA值
    - Android：
        - Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
        - Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30       
    - FireFox：
        - Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0
    - Google Chrome：
        - Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36
        - Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19
    - IOS：
        - Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3
- 设置UA的两种方式：
    - heads
    - add_header
## ProxyHandler(代理服务器)
- 为了防止IP被封，爬虫需要伪装自身IP，常用代理
- 获取代理服务器的地址：
    - www.xicidaili.com
    - www.goubanjia.com
- 代理也不允许频繁访问某一个固定网站，所以，代理一定要很多很多
- 基本使用步骤：
    - 设置代理地址
    - 创建ProxyHandler
    - 创建Opener
## Cookie和Session
- cookie是发送给用户的一段信息，session是保存在服务器上的对应的另一半用户信息，用来鉴别用户身份；类似于古代的虎符
- cookie与session的区别：
    - 存放位置不同
    - cookie不安全
    - session保存在服务器上一段时间，会过期
    - 单个cookie保存数据不超过4K，很多浏览器限制一个站点最多保存20个（非HTTP协议标准）
- session的存放位置
    - 存在server端
    - 存在内存或数据库中
- cookie相关
    - http模块包含一些关于cookie的模块，可以方便的操作cookie
        - CookieJar
            - 管理存储cookie，向传出的http请求添加cookie；
            - cookie存储在内存中，CookieJar实例回收后cookie将消失
        - FileCookieJar(filename, delayload=None, policy=None):
            - 使用文件管理cookie
        - MozillaCookieJar(filename, delayload=None, policy=None):
            - 创建于mocilla浏览器cookie.TXT兼容的FileCookieJar实例
        - LwpCookieJar（filename, delayload=None, policy=None):
            - 创建于libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
        - 关系：CookieJar --> FileCookieJar --> MozillaCookieJar & LwpCookieJar
## SSL
- SSL证书就是指遵守SSL安全套接层协议的服务器数字证书(SercureSocketLayer)
- 美国网景公司开发
- CA(CertificateAuthority)是数字证书认证中心，是发放、管理、废除数字证书的授信人的第三方机构
- 遇到不信任的证书，需要单独处理
## JS加密
- 有的反爬虫机制采用js对需要传输的数据进行加密处理（通常是MD5）
- JS必须在客户端执行，而且是明文代码，所以加密意义不大
- 在线格式化JS：http://tool.oschina.net/codeformat/json
## AJAX
- 异步请求
- 一般使用json格式

# Requests
- 更简洁
- 继承了urllib的所有特征
- 底层使用urllib3
- 开源：https://github.com/requests/requests
- 配套中文文档： http://docs.python-requests.org/zh_CN/latest/index.html
- 安装：conda install request
## GET
- requests.get(url)
- requests.request('get', url)
## POST
- rsp = requests.post(url, data=data)
- data,headers要求dict类型
## proxy
- 代理有可能报错，如果使用人数多，考虑安全问题，可能会被强行关闭
- 示例：
    - proxies = { 'http': 'address of proxy', 'https': 'address of proxy'}
    - rsp = requests.request('get', url, proxies = proxies)
## 用户验证
- 代理验证
    - 可能需要使用HTTP basic Auth
    - proxy = { 'http': 'username:password@192.168.1.1:8888' }
    - rsp = requests.get(url, proxies=proxy)
- web客户端验证
    - 添加auth=(username, password)
    - auth = ('test1', '123456')
    - rsp = requests.get(url, auth=auth)
## Cookie
- requests可以自动处理cookie信息
- 示例：
    - rsp = requests.get(url)
    - cookiejar = rsp.cookies
    - cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
## session
- 和服务器端的session不同
- 模拟一次对话，从客户端连接服务器开始，到客户端浏览器断开
- 能让我们跨请求时保持某些参数，比如，在同一个session实例发出的所有请求之间保持cookie
- 示例：
    - ss = requests.session()
    - headers = { 'User-Agent': 'xxx'}
    - data = { 'name': 'xxx' }
    - ss.post( url, data=data, headers=headers)
    - rsp = ss.get( url )
## https请求验证SSL证书
- 参数verify表示是否需要验证SSL证书，默认为True
- rsp = request.get( url, verify=False )
