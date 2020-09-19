import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

api = webdriver.Chrome()
# api.get("file:///C:/Users/ASUS/Desktop/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")
# api.get("file:///C:/Users/ASUS/Desktop/pagetest/pagetest/drag.html")
# api.get("file:///C:/Users/ASUS/Desktop/pagetest/pagetest/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")

#浏览器最大化
api.maximize_window()  # 最答化
# api.refresh()  #刷新
# time.sleep(2)
# bt= api.title
# print(bt)
# url= api.current_url
# print(url)

#鼠标
# a = api.find_element_by_tag_name("button")
# a = api.find_element_by_id("div1")
# b = api.find_element_by_id("div2")
# a.send_keys("admin")
# ActionChains(api).context_click(a).perform()  #选中元素点击右键
# ActionChains(api).double_click(a).perform()  #选中元素双击左键
# ActionChains(api).drag_and_drop(a,b).perform()  #选中元素拖拽
# ActionChains(api).move_to_element(a).perform()   #选中元素悬停


#键盘
# yong = api.find_element_by_id("userA")
# yong.send_keys("admin1")
# time.sleep(2)
# yong.send_keys(Keys.BACK_SPACE)
# time.sleep(2)
# yong.send_keys(Keys.CONTROL,'a')
# yong.send_keys(Keys.CONTROL, 'c')
# time.sleep(2)
# dian = api.find_element_by_id('telA')
# dian.send_keys(Keys.CONTROL,'v')


#元素等待
# api.implicitly_wait(20)
# ys = api.find_element_by_xpath("//*[contains(@placeholder, '延时')]")
# ys.send_keys("admin")

# xs = WebDriverWait(api,20,0.5).until(lambda api : api.find_element_by_xpath("//*[contains(@placeholder, '延时')]"))
# xs.send_keys("admin")

#下拉框
# time.sleep(1)
# s = Select(api.find_element_by_xpath('//*[@id="selectA"]'))
# time.sleep(1)
# s.select_by_value("gz")
# time.sleep(2)
# s.select_by_index(1)
# time.sleep(1)
# s.select_by_visible_text("深圳")

#弹出框
# api.find_element_by_xpath("//*[@id='alerta']").click()
# time.sleep(2)
# a = api.switch_to.alert  #找到弹出框
# time.sleep(2)
# a.accept()
# api.find_element_by_id("userA").send_keys("admin")

#滚动条
# js1 = "window.scrollTo(0,10000)"  #移动滚动条到最底
# js2 = "window.scrollTo(0,0)"
# time.sleep(2)
# api.execute_script(js1)
# time.sleep(2)
# api.execute_script(js2)

#切换页面
# api.find_element_by_id("userA").send_keys("admin")
# api.switch_to.frame(api.find_element_by_id("idframe1"))  #切换到指定的页面（frame）里面
# api.find_element_by_id("userA").send_keys("adminA")
# time.sleep(2)
# api.switch_to.default_content()  #返回到默认页面
# api.find_element_by_id("telA").send_keys("13800000000")
# time.sleep(2)
# api.switch_to.frame(api.find_element_by_id("idframe2"))
# api.find_element_by_id("userA").send_keys("adminB")
# time.sleep(2)
# api.switch_to.default_content()
# api.find_element_by_xpath("/html/body/div/div[1]/fieldset/form/p[4]/input").send_keys("123@qq.com")


#切换窗口
# api.implicitly_wait(10)
# #新窗口打开新浪
# print(api.current_window_handle)
# api.find_element_by_partial_link_text("访问").click()
# print(api.current_window_handle)
# handles = api.window_handles
# time.sleep(3)
# #在新窗口搜索admin
# api.switch_to.window(handles[1])
# sousuo = api.find_element_by_class_name("inp-txt")
# sousuo.clear()
# sousuo.send_keys("admin")

#截图
# api.find_element_by_id("userA").send_keys("admin")
# api.get_screenshot_as_file("./jietu/123__{}.png".format(time.strftime("%Y%m%d%H%M%S")))


#记录COOKIE
api.get("http://www.baidu.com/")
api.add_cookie({"name":"BDUSS","value":"EFRTGdzZ2lNaGdoc3hQc1FGbU9Odk5OSjYxTmhRMzByLWphNzRHS0RxN0hnNEZmSUFBQUFBJCQAAAAAAAAAAAEAAAAw9dt4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMf2WV~H9llfT"
})
time.sleep(3)
api.refresh()



time.sleep(3)
api.quit()