import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    rez = int(num1.text) + int(num2.text)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(rez))

    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()

finally:
    time.sleep(10)
    browser.quit()