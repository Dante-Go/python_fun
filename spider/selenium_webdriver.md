# 动态HTML介绍
- javaScript
- jQuery
- Ajax
- DHTML
- python采集动态数据：
    - 从javascript代码入手采集
    - Python第三方库运行JavaScript，直接采集浏览器的页面
# Selenium + PhantomJS
## Selenium : web自动化测试工具
- 自动加载页面
- 获取数据
- 截屏
- 安装：pip install selenium==2.48.0
- 官网：http://selenium-python.readthedocs.io/index.html
## PhantomJS(幽灵浏览器)
- 基于Webkit的无界面浏览器
- 官网：http://phantomjs.org/download.html
### selenium库的WebDriver可以与页面上的元素交互，模拟人工操作
## Chrome + chromedriver
- 安装时，注意版本对应关系
## Selenium操作
- 获取UI元素
    - find_element_by_id
    - find_elements_by_name
    - find_elements_by_xpath
    - find_elements_by_link_text
    - find_elements_by_partial_link_text
    - find_elements_by_tag_name
    - find_elements_by_class_name
    - find_elements_by_css_selector
- 基于UI元素模拟操作
    - 单机
    - 右键
    - 拖拽
    - 输入
    - 通过导入ActionsChains类操作
    
