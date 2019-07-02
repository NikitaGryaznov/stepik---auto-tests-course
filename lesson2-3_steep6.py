from selenium import webdriver
import math
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
#или
#browser.get("http://suninjuly.github.io/redirect_accept.html")
browser = webdriver.Chrome()


button = browser.find_element_by_css_selector("button.btn").click()
browser.switch_to.window(browser.window_handles[1])
#или
#new_window = browser.window_handles[1]
#browser.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x = browser.find_element_by_id("input_value").text
y = calc(x)

input1 = browser.find_element_by_id("answer").send_keys(y)
button = browser.find_element_by_css_selector("button.btn").click()
#Строка для срабатывания button.click()