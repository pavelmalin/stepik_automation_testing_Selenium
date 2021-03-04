#'''
# Задание: ждем нужный текст на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
# 1.Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser = webdriver.Chrome()
    browser.get(link)

# 2.Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

# 3.Нажать на кнопку "Book"
    button = browser.find_element_by_id("book")
    button.click()

# 4.Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x = browser.find_element_by_id("input_value")
    x = x.text
    z = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(z)

# 5.Нажать кнопку "Submit"
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
#'''








