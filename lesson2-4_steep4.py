from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
time.sleep(1) #В отличии от теста 2-4_steep3 добавлен time.sleep()

button = browser.find_element_by_id("check").click()
message = browser.find_element_by_id("check_message")
assert "успешно" in message.text