from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

button = WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.ID, "book")))
button.click()

message = browser.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
assert "успешно" in message.text

button1 = browser.find_element_by_css_selector("button.btn").click() # Не работает
#Строка для срабатывания button.click()