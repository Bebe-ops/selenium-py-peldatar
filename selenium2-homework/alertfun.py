#  A tanultak alapján az összes alert funkcióra írj selenium kódot.
#  A prompt-nál teszteld le, hogy a beírt érték megjelenik-e egy paragraf tagben, miután eltűnt az alert.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())


def find_element_and_click(my_xpath):  # elem kikeresés és aktiválás
    element = driver.find_element_by_xpath(my_xpath)
    element.click()
    return element


# tests data
expected_alert_text = 'I am alert'
expected_confirm_text = 'I am confirm'
prompt_input_text = "Yeah! It's working!"
expected_d_click_text = 'You double clicked me!!!, You got to be kidding me'
try:
    driver.get("http://localhost:9999/alert_playground.html")

    def alert_and_conf_b_close(xp):  # alert és confirm lekezelése
        find_element_and_click(xp)  # meghívom a függvényem
        alert = driver.switch_to.alert  # alertre kapcsolom a webdrivert
        if alert.text == 'I am alert':  # szövegek ellenőrzése
            assert (alert.text == expected_alert_text)
            print("Alert text is OK!")
        elif alert.text == expected_confirm_text:
            assert(alert.text == 'I am confirm')
            print("Confirm text is OK!")
        time.sleep(2)
        alert.accept()  # felugró bezárása


    alert_and_conf_b_close('//input[@value="Alert"]')  # meghívom a függvényemet az alertre
    alert_and_conf_b_close('//input[@value="Confirmation Box"]')  # és a confirmra

    # prompt kezelése (onclick esemény)
    find_element_and_click('//input[@value="Prompt"]')
    prompt = driver.switch_to.alert
    prompt.send_keys(prompt_input_text)
    time.sleep(1)
    prompt.accept()
    assert driver.find_element_by_xpath('//p[@id="demo"]').text == f'You entered: {prompt_input_text}'
    print('Prompt text is OK!')

    # double-click kezelése
    double_btn = driver.find_element_by_xpath('//input[@value="Double Click Me"]')
    action = ActionChains(driver)
    action.double_click(double_btn).perform()
    alert = driver.switch_to.alert
    assert alert.text == expected_d_click_text
    print('Double click alert is OK!')
    time.sleep(1)
    alert.accept()
except AssertionError:
    print('The written text does not match the expected result.')
finally:
    driver.close()
