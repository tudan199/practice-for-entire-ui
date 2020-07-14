from selenium import webdriver
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
print(sys.path)
# if this can push to git
sys.path.append('C:/Users/eagle/Desktop/practise/practice for entire ui/driver')
driver=webdriver.Chrome(executable_path="./driver/chromedriver.exe")
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('great!')

WebDriverWait(driver,10).until(lambda  s: s.find_element('id','su')).click()
driver.maximize_window()
time.sleep(5)
driver.quit()