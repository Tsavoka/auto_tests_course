# Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное 
# решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки 
# сообщений. Ваша задача — реализовать автотест со следующим сценарием действий: 
#  открыть страницу 
#  авторизоваться на странице со своим логином и паролем
#  ввести правильный ответ (поле перед вводом должно быть пустым)
#  нажать кнопку "Отправить" 
#  дождаться фидбека о том, что ответ правильный 
#  проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
# Опциональный фидбек — это текст в черном поле.
# Правильным ответом на задачу в заданных шагах является число:
#  answer = math.log(int(time.time()))
# Используйте маркировку pytest для параметризации и передайте в тест список ссылок в 
# качестве параметров.
# Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте 
# нужные ожидания, чтобы тесты работали стабильно. 
# В упавших тестах найдите кусочки послания. Тест должен падать, если текст в 
# опциональном фидбеке не совпадает со строкой "Correct!" Соберите кусочки текста в 
# одно предложение и отправьте в качестве ответа на это задание. 
# Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено
# правильное локальное время (https://time.is/ru/). Ответ для каждой задачи нужно 
# пересчитывать отдельно, иначе они устаревают. 

import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

login = "login"         
password = "password"   

result = ''

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print(result)


def answer():
    return math.log(int(time.time()))


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_twin_peaks(browser, link):
    global result
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element(By.CLASS_NAME, "navbar__auth_login").click()
    browser.find_element(By.ID, "id_login_email").send_keys(login)
    browser.find_element(By.ID, "id_login_password").send_keys(password)
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
    time.sleep(10)                                              # загрузка сайта после регистрации
    browser.find_element(By.CLASS_NAME, "ember-text-area").send_keys(answer())
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    text = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    browser.find_element(By.CLASS_NAME, 'again-btn').click()    # перезагрузка для последующего тестирования

    try:
        assert text == 'Correct!'
    except AssertionError:
        result += text

# The owls are not what they seem! OvO