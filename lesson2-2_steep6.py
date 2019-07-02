from selenium import webdriver
import math

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element_by_id("input_value").text
y = calc(x)

# Блок скролла страницы вниз до элемента "button" при помощи метода "execute_script"
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

input1 = browser.find_element_by_id("answer").send_keys(y)
chekbox = browser.find_element_by_css_selector("[id='robotCheckbox']").click()
radiobutton = browser.find_element_by_css_selector("[id='robotsRule']").click()
button = browser.find_element_by_css_selector("button.btn").click()
#Строка для срабатывания button.click()