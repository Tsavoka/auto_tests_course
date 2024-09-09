# Попробуйте оформить тесты из первого модуля в стиле unittest.
# Создайте новый файл
# Создайте в нем класс с тестами, который должен наследоваться от 
# unittest.TestCase по аналогии с предыдущим шагом
# Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
# Оформите финальные проверки в тестах в стиле unittest, например, используя 
# проверочный метод assertEqual
# Запустите получившиеся тесты из файла 
# Просмотрите отчёт о запуске и найдите последнюю строчку 
# Отправьте эту строчку в качестве ответа на это задание 
# Обратите внимание, что по задумке должно выбрасываться исключение 
# NoSuchElementException во втором тесте. Если вы использовали конструкцию try/except, 
# здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае,
# здесь)!
# Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже 
# при наличии неожиданного исключения. 

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fill_form(link):
    with webdriver.Chrome() as browser:
        browser.get(link)

        browser.find_element(By.CLASS_NAME, "first_block .first").send_keys("Abyr")
        browser.find_element(By.CLASS_NAME, "first_block .second").send_keys("Valg")
        browser.find_element(By.CLASS_NAME, "first_block .third").send_keys("email")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        time.sleep(1)   # Проверяем, что смогли зарегистрироваться

        return browser.find_element(By.TAG_NAME, "h1").text
        

class TestUniqSel(unittest.TestCase):
    def test_first_link(self):
        welcome_text = fill_form('http://suninjuly.github.io/registration1.html')
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
   
    def test_second_link(self):
        welcome_text = fill_form("https://suninjuly.github.io/registration2.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
 
  
if __name__ == "__main__":
    unittest.main()