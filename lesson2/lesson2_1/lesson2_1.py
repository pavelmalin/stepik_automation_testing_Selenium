'''
#Задание: кликаем по checkboxes и radiobuttons (капча для роботов)

from selenium import webdriver
import time
import math

#Посчитать математическую функцию от x (код для этого приведён ниже).
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Отметить checkbox "I'm the robot".
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''
#'''
# Задание: поиск сокровища с помощью get_attribute
from selenium import webdriver
import time
import math

#Посчитать математическую функцию от x (код для этого приведён ниже).
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Находим атрибут valuex
    x_element = browser.find_element_by_id("treasure")
    # Получаем значение атрибута valuex
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Отметить checkbox "I'm the robot".
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
#'''