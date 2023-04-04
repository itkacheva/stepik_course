import time
from selenium.webdriver.common.by import By


def test_guest_should_see_add_button(browser):
    time.sleep(30)
    add_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_button, 'Button is not find'