# 页面解析和数据提取
## 结构数据：先有结构，再谈结构
- JSON文件：
    - JSON Path
    - 转换成Python类型进行操作（json类）
- XML文件：
    - 转换成python类型（xmltodict）
    - XPath
    - CSS选择器
    - 正则
## 非结构化数据：先有数据，再谈结构
- 文本、电话号码、邮箱地址
    - 通常处理此类数据，使用正则表达式
- HTML文件
    - 正则
    - XPath
    - CSS选择器
# 正则表达式
## 正则常用方法：
- match: 从开始位置开始查找，一次匹配
- search: 从任何位置查找，一次匹配
- findall: 全部匹配，返回list
- finditer: 全部匹配，返回迭代器
- split: 分个字符串，返回列表
- sub: 替换
## 匹配中文
- 中文Unicode码主要在[u4e00-u9fa5]
## 贪婪与非贪婪
- python中，数量词默认贪婪匹配
- 示例：
    - 查找abbbbbcc
    - re = ab*
    - 贪婪匹配：abbbbb
    - 非贪婪匹配：a
# XML
- Extensable Markup Language
- http://www.w3school.com.cn/xml/index.asp
- 概念：父节点、子节点、先辈节点、兄弟节点、后代节点
# XPATH
- XML Path Language, 是一门在XML文档中查找信息的语言；
- http://www.w3school.com.cn/xpath/index.asp
## XPath开发工具：
- XMLQuire：开源的XPath表达式工具
- Xpath Helper：chrome插件
- XPath Checker：FireFox插件
## 常用表达式：
- nodename: 选择nodename的所有子节点
- /: 从根节点开始查找
- //: 选取元素，不考虑元素具体位置
- .: 当前节点
- ..: 父节点
- @: 选取属性
## 谓语(predicates):
- 用于定位某个具体的节点，放置于[]中
- /nodename/childnodename[1] : 选择nodename下第一个childnodename节点
- /nodename/childnodename[last()] : 选择nodename下最后一个childnodename节点
- /nodename/childnodename[last()-1] : 选择倒数第二个节点
- /nodename/childnodename[position()<3] : 选择前两个节点
- /nodename/childnodename[@lang] : 选择有lang属性的元素
- /nodename/childnodename[@lang="cn"] : 选择含有lang属性，且其值为cn的元素
- /nodename/childnodename[@price < 90]/title : 选择含有price属性，其值小于90的节点的title子节点
## 通配符：
- * : 匹配任何节点
- @* : 匹配任何属性
- node() : 匹配任何类型节点 
## 多个路径
- //nodename/node | //nodenameB/node2 : 选择nodename下node和nodenameB下node2
# lxml库
- HTML/XML解析器
- http://lxml.de/index.html
- 功能：
    - 解析HTML
    - 文件读取
    - etree和XPath配合使用
# CSS 选择器 BeautifulSoup4
- http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
## 常用提取信息工具的比较：
    - 正则：很快、不好用、不需要安装
    - beautifulsoup: 慢、使用简单、安装简单
    - lxml: 比较快、使用简单、安装一般
## 四大对象
    -  
