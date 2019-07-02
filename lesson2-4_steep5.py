from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("check").click()
message = browser.find_element_by_id("check_message")
assert "успешно" in message.text
#Улучшим тест с помощью неявных ожиданий. Для этого нам нужно будет убрать time.sleep() и добавить одну строчку с методом implicitly_wait: