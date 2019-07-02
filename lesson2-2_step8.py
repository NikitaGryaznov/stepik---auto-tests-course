from selenium import webdriver
import time
import os 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
# Ваш код, который заполняет обязательные поля
input1 = browser.find_element_by_css_selector('[name="firstname"]')
input1.send_keys("Ivan")
input2 = browser.find_element_by_css_selector('[name="lastname"]')
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector('[name="email"]')
input3.send_keys("qwer@qwer.qw")
# Отправляем заполненную форму
button1 = browser.find_element_by_css_selector('[name="file"]')
button1.click()#работает

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
#current_dir = os.path.dirname(r'C:\Users\ngryaznov\selenium_course')
file_path = os.path.join(current_dir, 'pyfile.txt')         # добавляем к этому пути имя файла 
button1.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()
# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

