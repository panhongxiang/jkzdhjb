import time

from selenium import webdriver
from selenium.webdriver.common.by import By

a = webdriver.Chrome()

a.get("file:///C:/Users/ASUS/Desktop/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")  #打开浏览器输入url
# a.find_element_by_id("passwordA").send_keys("123456")  #通过id定位元素
# a.find_element_by_tag_name("input").send_keys("admin") # 通过标签名（tag_name）定位元素
# a.find_element_by_class_name("dzyxA").send_keys("123@qq.com") #通过类明（class_name)定位元素
# a.find_element_by_link_text("打开百度").click()  #通过超链接全部文字定位元素
# a.find_element_by_partial_link_text("访问").click()  # 通过超链接部分文字定位元素
# a.find_elements_by_tag_name("input")[1].send_keys("123456") # 使用标签定位一组元素 element需要加s
# a.find_element_by_xpath("//*[@id='userA']").send_keys("admin") #通过xpath相对路径定位元素
# a.find_element_by_xpath("/html/body/div/fieldset/form/p[4]/input").send_keys("123456")#通过xpath绝对路径定位元素
# a.find_element_by_xpath("//*[@id= 'userA']").send_keys("123456")  #通过元素属性定位元素
# a.find_element_by_xpath("//*[@type= 'text'and @name= 'telA']").send_keys('123456') #通过属性与逻辑结合定位元素
# a.find_element_by_xpath("//*[@id='p1']/input").send_keys("123456") #通过层级与属性结合定位元素
# a.find_element_by_xpath('//*[contains(@id, "rA")]').send_keys("123456")  #通过属性中含有xxx的元素
# a.find_element_by_css_selector("#userA").send_keys("123456")  #根据元素id属性来选择
# a.find_element_by_css_selector('.telA').send_keys("123456")   #根据元素class属性来选择
# a.find_element_by_css_selector("button").click()   #根据元素的标签名选择
# a.find_element_by_css_selector("[type='password']").send_keys("123456")   #根据元素的属性名和值来选择
# a.find_element_by_css_selector("div[class='zc'] input").send_keys("123456")   #根据元素的父子关系来选择
# a.find_element(By.ID, "userA").send_keys("admin")  #导包定位元素

time.sleep(3)

a.quit()