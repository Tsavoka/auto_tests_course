# Задание: поиск сокровища с помощью get_attribute
# В данной задаче вам нужно с помощью роботов решить ту же математическую 
# задачу, как и в прошлом задании. Но теперь значение переменной х спрятано 
# в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с 
# изображением сундука.
# Ваша программа должна:
# - Открыть страницу http://suninjuly.github.io/get_attribute.html.
# - Найти на ней элемент-картинку, который является изображением сундука с 
# сокровищами.
# - Взять у этого элемента значение атрибута valuex, которое является 
# значением x для задачи.
# - Посчитать математическую функцию от x (сама функция остаётся неизменной).
# - Ввести ответ в текстовое поле.
# - Отметить checkbox "I'm the robot".
# - Выбрать radiobutton "Robots rule!".
# - Нажать на кнопку "Submit".
# - Для вычисления значения выражения в п.4 используйте функцию calc(x) 
# из предыдущей задачи.
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть 
# ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже 
# и нажмите кнопку "Submit", чтобы получить баллы за задание.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    #x = x_element.text
    y = calc(x)

    button = browser.find_element(By.ID, 'answer')
    button.send_keys(y)

    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    submit = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()