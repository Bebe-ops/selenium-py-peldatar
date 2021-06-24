from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/kitchensink.html")

bmw_radio = driver.find_element_by_id("bmwradio")
car_select = driver.find_element_by_id("carselect")
alert_input = driver.find_element_by_name("enter-name")
input_show_hide = driver.find_element_by_name("show-hide")
multi_select_apple = driver.find_element_by_xpath('//select[@id="multiple-select-example"]/option[1]')
bmw_check = driver.find_element_by_xpath('//input[@id="bmwcheck"]')


def get_attr():
    multi_sel_a = multi_select_apple.get_attribute("value")
    val_chb = bmw_check.get_attribute("value")
    print(multi_sel_a)
    print(val_chb)


get_attr()

driver.close()
