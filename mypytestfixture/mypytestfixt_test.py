# 006 Feladat: Fixture, setup, teardown,
# alertfun pytest átalakítása -> fixture használata a böngésző inicializálására
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # headless
    driver.get('http://localhost:9999/alert_playground.html')
    return driver


def test_alerts_text(browser):
    time.sleep(3)

    def find_element_and_click(my_xpath):
        element = browser.find_element_by_xpath(my_xpath)
        element.click()
        return element

    # tests data
    expected_alert_text = 'I am alert'
    expected_confirm_text = 'I am confirm'
    prompt_input_text = "Yeah! It's working!"
    expected_d_click_text = 'You double clicked me!!!, You got to be kidding me'

    def alert_and_conf_b_close(xp, expected_data):  # alert és confirm lekezelése
        find_element_and_click(xp)
        alert = browser.switch_to.alert
        assert alert.text == expected_data
        time.sleep(2)
        alert.accept()

    alert_and_conf_b_close('//input[@value="Alert"]', expected_alert_text)  # alert
    alert_and_conf_b_close('//input[@value="Confirmation Box"]', expected_confirm_text)  # confirmation box

    # prompt kezelése (onclick esemény)
    find_element_and_click('//input[@value="Prompt"]')
    prompt = browser.switch_to.alert
    prompt.send_keys(prompt_input_text)
    time.sleep(1)
    prompt.accept()
    assert browser.find_element_by_xpath('//p[@id="demo"]').text == f'You entered: {prompt_input_text}'

    # double-click kezelése
    double_btn = browser.find_element_by_xpath('//input[@value="Double Click Me"]')
    action = ActionChains(browser)
    action.double_click(double_btn).perform()  # meghívom a double click-et az elemre
    d_c_alert = browser.switch_to.alert  # alertre kapcsolom a webdrivert
    assert d_c_alert.text == expected_d_click_text
    time.sleep(1)
    d_c_alert.accept()


def test_elements_enabled(browser):
    buttons = browser.find_elements_by_tag_name('input')
    for _ in buttons:
        assert _.is_enabled()
