from selenium import webdriver
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex") #Метод get_attribute нужен чтобы узнать значение атрибута элемента
y = calc(x)
input1 = browser.find_element_by_css_selector('#answer').send_keys(y)

chekbox = browser.find_element_by_css_selector("[id='robotCheckbox']").click()
radiobutton = browser.find_element_by_css_selector("#robotsRule").click()

button = browser.find_element_by_css_selector("button.btn").click()
#Строка для срабатывания button.click()