from selenium import webdriver
import math
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

button = browser.find_element_by_css_selector("button.btn").click()
confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_id("input_value").text
y = calc(x)
input1 = browser.find_element_by_id("answer").send_keys(y)
button = browser.find_element_by_css_selector("button.btn").click()
#Строка для срабатывания button.click()