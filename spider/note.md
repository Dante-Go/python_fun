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
