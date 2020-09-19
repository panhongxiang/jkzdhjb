import time

from selenium import webdriver

bd = webdriver.Chrome()

bd.get("http://www.baidu.com")
bd.find_element_by_id("kw").send_keys("华为")
bd.find_element_by_id("su").click()
time.sleep(3)

bd.quit()