from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

a = browser.find_element_by_id("num1").text
b = browser.find_element_by_id("num2").text
c = (str(int(a)+int(b)))
select = Select(browser.find_element_by_css_selector(".custom-select"))
select.select_by_visible_text(c)

button = browser.find_element_by_css_selector("button.btn")
button.click()
#Строка для срабатывания button.click()
