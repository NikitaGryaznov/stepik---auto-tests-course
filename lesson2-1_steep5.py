from selenium import webdriver
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

chekbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
chekbox.click()
radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
radiobutton.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
#Строка для срабатывания button.click()