# У нас уже есть простой тест из предыдущего шага, который проверяет возможность 
# зарегистрироваться на сайте. Однако разработчики решили немного поменять 
# верстку страницы, чтобы она выглядела более современной. Обновленная страница 
# доступна по другой ссылке. К сожалению, в процессе изменений они случайно внесли
# баг в форму регистрации.
# Попробуйте запустить код из предыдущего шага, указав в качестве начальной 
# страницы новую ссылку. Если ваш тест упал с ошибкой NoSuchElementException, это 
# означает, что вы выбрали правильные селекторы и смогли обнаружить баг, который 
# создали разработчики. Это хорошо! Значит, ваши тесты сработали как надо. Пугаться
#  не стоит, здесь ошибка в приложении которое вы тестируете, а не в вашем тесте. 
# Если же ваш тест прошел успешно, то это означает, что тест пропустил серьезный 
# баг. В этом случае попробуйте поменять селекторы, сделав их уникальными. После 
# изменения убедитесь, что ваш тест исправно проходит в старой версии страницы.
# Чтобы получить максимальное количество баллов, прежде чем отправлять решение на 
# рецензию, самостоятельно убедитесь в том что: 
# - Тест успешно проходит на странице http://suninjuly.github.io/registration1.html
# - Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html
# - Используемые селекторы должны быть уникальны


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # Линк для первого теста, в котором все работает:
    # link = "https://suninjuly.github.io/registration1.html"

    # Линк, в котором ловим NoSuchElementException
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных полей
    input1 = browser.find_element(By.CLASS_NAME, 'first_block .first')
    input1.send_keys('Abyr')
    input2 = browser.find_element(By.CLASS_NAME, 'first_block .second')
    input2.send_keys('Valg')
    input3 = browser.find_element(By.CLASS_NAME, 'first_block .third')
    input3.send_keys('email')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # Ждем загрузки страницы
    time.sleep(1)

    # Находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # Записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Ожидание, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрытие браузера после всех манипуляций
    browser.quit()
    