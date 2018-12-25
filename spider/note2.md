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
