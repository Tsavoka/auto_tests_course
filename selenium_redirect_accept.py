# В этом задании после нажатия кнопки страница откроется в новой вкладке, 
# нужно переключить WebDriver на новую вкладку и решить в ней задачу.
# Сценарий для реализации выглядит так:
# - Открыть страницу http://suninjuly.github.io/redirect_accept.html
# - Нажать на кнопку
# - Переключиться на новую вкладку
# - Пройти капчу для робота и получить число-ответ
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть 
# ограничение по времени), вы увидите окно с числом. Отправьте полученное 
# число в качестве ответа на это задание.


from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log as ln, sin
import time


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    time.sleep(5)
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, 'input_value').text
    y = ln(abs(12*sin(int(x))))

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    rez = browser.switch_to.alert.text
    print(rez.split(': ')[-1])

finally:
    browser.quit()