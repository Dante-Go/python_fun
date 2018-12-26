from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'http://www.baidu.com'

driver = webdriver.Chrome()
driver.get(url)

text = driver.find_element_by_id('wrapper').text
print(text)
print(driver.title)
driver.save_screenshot('index.png')

driver.find_element_by_id('kw').send_keys(u'三沙市')
driver.find_element_by_id('su').click()
time.sleep(5)
driver.save_screenshot('sansha.png')
print(driver.get_cookies())

# ctrl + a
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# ctrl + x
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

driver.find_element_by_id('kw').send_keys(u'南沙')
driver.find_element_by_id('kw').send_keys(Keys.RETURN)
time.sleep(5)
driver.save_screenshot('nansha.png')

driver.find_element_by_id('kw').clear()
driver.quit()
