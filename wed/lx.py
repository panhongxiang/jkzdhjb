import time

from selenium import webdriver

js = webdriver.Chrome()
js.get("file:///C:/Users/ASUS/Desktop/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")
js.find_element_by_id("userA").send_keys("admin")
js.find_element_by_id("passwordA").send_keys("123456")
js.find_element_by_id("telA").send_keys("18611111111")
js.find_element_by_name("emailA").send_keys("123@qq.com")
time.sleep(3)
js.find_element_by_id("telA").clear()
js.find_element_by_id("telA").send_keys("18600000000")
time.sleep(3)
js.find_element_by_xpath('/html/body/div/fieldset/form/p[5]/button').click()
time.sleep(3)
js.quit()