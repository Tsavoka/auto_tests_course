# Попробуем теперь написать программу, которая будет бронировать нам дом 
# для отдыха по строго заданной цене. Более высокая цена нас не
#  устраивает, а по более низкой цене объект успеет забронировать кто-то 
# другой.
# В этой задаче вам нужно написать программу, которая будет выполнять 
# следующий сценарий:
# - Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# - Дождаться, когда цена дома уменьшится до $100 (ожидание нужно 
# установить не меньше 12 секунд)
# - Нажать на кнопку "Book"
# - Решить уже известную нам математическую задачу (используйте ранее 
# написанный код) и отправить решение
# - Чтобы определить момент, когда цена аренды уменьшится до $100, 
# используйте метод text_to_be_present_in_element из библиотеки 
# expected_conditions.
# Если все сделано правильно и быстро, то вы увидите окно с числом. 
# Отправьте его в качестве ответа на это задание.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log as ln, sin


with webdriver.Chrome() as browser: 
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    #browser.implicitly_wait(5)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.ID, 'input_value').text
    y = ln(abs(12*sin(int(x))))

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    browser.find_element(By.ID, 'solve').click()
    print(browser.switch_to.alert.text.split(': ')[-1])
    