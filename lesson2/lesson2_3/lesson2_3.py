'''
# Задание: принимаем alert
from selenium import webdriver

import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
# 1.Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser = webdriver.Chrome()
    browser.get(link)

# 2.Нажать на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

# 3.Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

# 4.На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = browser.find_element_by_id("input_value")
    x = x.text
    z = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(z)

# 5.Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
'''
#'''
# Задание: переход на новую вкладку
from selenium import webdriver

import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
# 1.Открыть страницу http://suninjuly.github.io/redirect_accept.html
    browser = webdriver.Chrome()
    browser.get(link)

# 2.Нажать на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

# 3.Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

# 4.Пройти капчу для робота и получить число-ответ
    x = browser.find_element_by_id("input_value")
    x = x.text
    z = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(z)

# 5.Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
#'''








