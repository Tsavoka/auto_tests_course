import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log as ln
from math import sin

def calc(x):
    return str(ln(abs(12*sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value')
    y = calc(int(x.text))

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(str(y))

    browser.find_element(By.ID, 'robotCheckbox').click()

    button = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

finally:
    time.sleep(10)
    browser.quit()