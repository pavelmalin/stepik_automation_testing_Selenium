'''
# Работа со списками
# Задание: работа с выпадающим списком
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time 
import math

def calc(x,y):
    return str(int(x)+int(y))

#link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
# 1.Открыть страницу http://suninjuly.github.io/selects1.html
    browser = webdriver.Chrome()
    browser.get(link)

# 2.Подсчитать сумму заданных чисел
    x = browser.find_element_by_id("num1")
    y = browser.find_element_by_id("num2")
    x = x.text
    y = y.text
    z = calc(x,y)

# 3.Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z) # ищем элемент с текстом суммы

# 4.Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
'''
'''
# Задание на execute_script
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
# 1.Открыть страницу http://SunInJuly.github.io/execute_script.html
    browser = webdriver.Chrome()
    browser.get(link)

# 2.Считать значение для переменной x
    x = browser.find_element_by_id("input_value")
    x = x.text

# 3.Посчитать математическую функцию от x
    z = calc(x)

# 4. Проскроллить страницу вниз
    input1 = browser.find_element_by_tag_name("input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
  
# 5. Ввести ответ в текстовое поле.
    input1.send_keys(z)

# 6. Выбрать checkbox "I'm the robot".
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

# 7. Переключить radiobutton "Robots rule!".
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

# 8.Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
'''
#'''
# Задание: загрузка файла
from selenium import webdriver

import time 
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
# 1.Открыть страницу http://suninjuly.github.io/file_input.html
    browser = webdriver.Chrome()
    browser.get(link)

# 2.Заполнить текстовые поля: имя, фамилия, email
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("hfh@hhd")

# 3.Загрузить файл. 
#    Файл должен иметь расширение .txt и может быть пустым
# получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'file.txt')
    element1 = browser.find_element_by_css_selector("[type='file']")
    element1.send_keys(file_path)

# 4.Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
#'''








