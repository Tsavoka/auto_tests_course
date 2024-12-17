from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button(browser):
    browser.get(link)
    answer = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert len(answer) > 0, 'No button here'
