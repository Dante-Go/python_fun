# scrapy-shell
- https://segmentfault.com/a/1190000013199636?utm_source=tag-newest
- scrapy开发环境
## 启动
- Linux：scrapy shell 'url:xxx'
- windows: scrapy shell "url:xxx"
## 处理
- shell启动后，自动下载指定url的网页，下载完后保存在response变量中
## response
- response.body是网页的源码
- response.headers是返回的header信息
- response.xpath() 使用xpath语法选择元素
- response.css()使用css语法选取元素
## selector
- resonse.selector.xpath:
- response.selector.css
- selector.extract：把节点的内容用Unicode形式返回
- selector.re：用正则选取元素

# 分布式爬虫
## 单机爬虫的问题：
- 单机效率
- IO吞吐量
## 多爬虫问题
- 数据共享
## 需要的设施
- 共享队列
- 去重
## Redis
- 内存数据库
- 同时可以落地保存到硬盘
- 可以去重
- 可以把它理解成集dict，set，list的特性一体的设施
- 可以对保存的内容进行生命周期管理，设置过期时间
## 内容保存到数据库
- MongoDB
- Mysql等传统数据库
## 安装Scrapy_redis
- pip install scrapy_redis
- github.com/rolando/scrapy-redis
- scrapy-redis.readthedocs.org

# 推荐书籍
- Python爬虫开发与项目实战，范传辉，机械工业出版社
- 精通Python爬虫框架Scrapy， 李斌 翻译， 人民邮电出版社
- 崔庆才

