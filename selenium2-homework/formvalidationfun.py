# A tanultak alapján teszteld le az űrlap mező ellenőrző funkcióit.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/simplevalidation.html")

    # Üresen hagyott form signUp hover buborék ellenőrzése
    signup_btn = driver.find_element_by_id('test-button')
    ActionChains(driver).move_to_element(signup_btn).perform()  # submit fölé viszem az egeret
    msg = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'test-button'))).get_attribute('data-jsv-form-tooltip')
    print(msg)
    assert msg is not None
    assert msg == "Please complete all fields"

    required = []
    # REQUIRED ID LISTA ÖSSZEÁLLÍTÁSA (sorban) Kötelező input és select mezők
    all_input_elements = driver.find_elements_by_xpath('//input')  # összes input element id
    for i in all_input_elements:
        required.append(i.get_attribute("id"))

    required.remove("test-random-field")   # A nem kötelező mező-id-k eltávolítása
    required.remove("test-url-field")

    text_area_id = driver.find_element_by_id('test-random-textarea').get_attribute("id")  # required listába
    required.insert(6, text_area_id)

    select_elements = driver.find_elements_by_xpath('//select')  # össz.select mező required listába
    select_field_id = []
    for i in select_elements:
        select_field_id.append(i.get_attribute("id"))

    required.insert(7, select_field_id[0])
    required.insert(10, select_field_id[1])
    required.insert(11, select_field_id[2])

    check_box_id = [required[12], required[15], required[16]]  # chbox lista
    radio_id = required[13:15]  # radio lista

    del(required[12::])  # chboxok, radiok törlése required listából

    # ÜRESEN HAGYOTT MEZŐK (TC001)
    def empty_inp(my_id):  # Kötelező mezők kattintása
        driver.find_element_by_id(my_id).click()
    for i in required:  # required lista iteráció
        empty_inp(i)

    def check_double_click(my_id):
        for j in range(2):
            driver.find_element_by_id(my_id).click()
    for i in check_box_id:  # checkbox-ok dupla kattintása
        check_double_click(i)

    # ÜRESEN HAGYOTT MEZŐK HIBAÜZENETEK LISTÁJÁNAK ÖSSZEÁLLÍTÁSA
    error_msg = driver.find_elements_by_xpath('//div[@class="validate-field-error-message"]')
    err_msg_text = []
    for i in error_msg:
        if i.text == "":   # nem kötelező mezők: üres stringek nem kellenek
            continue
        else:
            err_msg_text.append(i.text)

    # ELLENŐRZÉS: megjelennek e a hibaüzenetek az üresen hagyott kötelező mezőknél (azonos számúak)
    time.sleep(2)
    assert len(required) + len(check_box_id) == len(err_msg_text) + 1  # (az uccsó 2 checkbox-nak közös hibaüzenete van)
    print("Minden üresen hagyott kötelező mezőhöz megjelent a hibaüzenet.")

    # ---------------------------------------------------------------------------------------------------------------
    # HELYTELEN ADATOK BEVITELE  (TC002)
    # Beviteli mezők külön listába (Select-ek nélkül)
    time.sleep(5)
    driver.get("http://localhost:9999/simplevalidation.html")
    input_fields = []
    for i in required:
        if i == required[7] or i == required[10] or i == required[11]:
            continue
        else:
            input_fields.append(i)

    invalid_test_data = ["geza@gmailcom", "123ab", "123ab", "a", "12345", "2021.01.01", "A", "411111111111", "asd12"]

    def invalid_inp(my_id, my_data):  # Kötelező input mezők kitöltése
        driver.find_element_by_id(my_id).send_keys(my_data)

    for a, b in zip(input_fields, invalid_test_data):  # függv.hívás - mezők kitöltése
        invalid_inp(a, b)

    # Helytelen adat hibaüzenetek kigyűjtése
    invalid_error_msg = driver.find_elements_by_xpath('//div[@class="validate-field-error-message"]')
    invalid_err_msg_text = []
    for i in invalid_error_msg:
        if i.text == "":   # nem kötelező mezők: üres stringek nem kellenek
            continue
        else:
            invalid_err_msg_text.append(i.text)

    for data, err in zip(input_fields, invalid_err_msg_text):
        assert err is not None
    assert len(input_fields) == len(invalid_err_msg_text)
    print("Minden mezőhöz megjelent a helytelen bevitel hibaüzenet.")

    # MINDEN KÖTELEZŐ ELEM KITÖLTÉSE HELYES ADATOKKAL TC003
    time.sleep(5)
    driver.get("http://localhost:9999/simplevalidation.html")

    valid_test_data = ["yardy@yarr.com", "123abc", "123abc", "1", "1234", "2021-01-01", "test", "4111111111111111", "111"]

    for a, b in zip(input_fields, valid_test_data):  # függv.hívás - beviteli mezők kitöltése
        invalid_inp(a, b)

    # selectek
    def select_value(xpath):
        element = driver.find_element_by_xpath(xpath)
        element.click()

    select_value('//*[@id="test-card-type"]/option[@value="VI"]')
    select_value('//*[@id="test-card-month"]/option[@value="1"]')
    select_value('//*[@id="test-card-year"]/option[@value="2025"]')

    # checkboxok
    def check_box(my_id):
        driver.find_element_by_id(my_id).click()

    for i in check_box_id:  # checkbox-ok dupla kattintása
        check_box(i)

    # radio
    driver.find_element_by_id('test-save-email-yes').click()

    # sign_in btn elérhető e
    time.sleep(2)
    signup_btn = driver.find_element_by_id('test-button').click()
finally:
    driver.close()
