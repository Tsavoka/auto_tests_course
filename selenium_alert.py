# В этой задаче вам нужно написать программу, которая будет выполнять 
# следующий сценарий:
# - Открыть страницу http://suninjuly.github.io/alert_accept.html
# - Нажать на кнопку
# - Принять confirm
# - На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть 
# ограничение по времени), вы увидите окно с числом. Отправьте полученное 
# число в качестве ответа на это задание.

from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    browser.switch_to.alert.accept()

    def answ(x):
        return log(abs(12*sin(int(x))))

    x = browser.find_element(By.ID, 'input_value').text
    y = answ(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    browser.quit()
