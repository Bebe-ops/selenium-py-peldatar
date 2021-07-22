# alertfun pytestesítése

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


class TestAlertFun(object):
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless
        self.driver.get('http://localhost:9999/alert_playground.html')

    def teardown(self):
        self.driver.close()

    def test_alerts_text(self):
        time.sleep(3)

        def find_element_and_click(my_xpath):
            element = self.driver.find_element_by_xpath(my_xpath)
            element.click()
            return element

        # tests data
        expected_alert_text = 'I am alert'
        expected_confirm_text = 'I am confirm'
        prompt_input_text = "Yeah! It's working!"
        expected_d_click_text = 'You double clicked me!!!, You got to be kidding me'

        def alert_and_conf_b_close(xp, expected_data):  # alert és confirm lekezelése
            find_element_and_click(xp)
            alert = self.driver.switch_to.alert
            assert alert.text == expected_data
            time.sleep(2)
            alert.accept()

        alert_and_conf_b_close('//input[@value="Alert"]', expected_alert_text)  # alert
        alert_and_conf_b_close('//input[@value="Confirmation Box"]', expected_confirm_text)  # confirmation box

        # prompt kezelése (onclick esemény)
        find_element_and_click('//input[@value="Prompt"]')
        prompt = self.driver.switch_to.alert
        prompt.send_keys(prompt_input_text)
        time.sleep(1)
        prompt.accept()
        assert self.driver.find_element_by_xpath('//p[@id="demo"]').text == f'You entered: {prompt_input_text}'

        # double-click kezelése
        double_btn = self.driver.find_element_by_xpath('//input[@value="Double Click Me"]')
        action = ActionChains(self.driver)
        action.double_click(double_btn).perform()  # meghívom a double click-et az elemre
        d_c_alert = self.driver.switch_to.alert  # alertre kapcsolom a webdrivert
        assert d_c_alert.text == expected_d_click_text
        time.sleep(1)
        d_c_alert.accept()

    def test_elements_enabled(self):
        buttons = self.driver.find_elements_by_tag_name('input')
        for _ in buttons:
            assert _.is_enabled()
