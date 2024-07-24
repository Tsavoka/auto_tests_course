# В этом задании в форме регистрации требуется загрузить текстовый файл.
# Напишите скрипт, который будет выполнять следующий сценарий:
# - Открыть страницу http://suninjuly.github.io/file_input.html
# - Заполнить текстовые поля: имя, фамилия, email
# - Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# - Нажать кнопку "Submit"


import os 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Abyr')
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Valg')
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('ljdqw')

    with open("file.txt", "w") as file:
        file.write("abyr")
    element = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname('file_path.py'))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

finally:
    time.sleep(10)
    browser.quit()
    