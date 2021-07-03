from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless
driver = webdriver.Chrome(ChromeDriverManager().install())


def get_attr():
    print(multi_select_apple.get_attribute("value"))
    print(bmw_check.get_attribute("value"))
    print(confirm_button.get_attribute("type"))


try:
    driver.get("http://localhost:9999/kitchensink.html")
    driver.find_element_by_id("bmwradio")
    driver.find_element_by_id("carselect")
    driver.find_element_by_name("enter-name")
    driver.find_element_by_name("show-hide")
    multi_select_apple = driver.find_element_by_xpath('//select[@id="multiple-select-example"]/option[1]')
    bmw_check = driver.find_element_by_xpath('//input[@id="bmwcheck"]')
    confirm_button = driver.find_element_by_id("confirmbtn")
    get_attr()
    print("test finished OK")
except NoSuchElementException as e:
    print('Element not found: ', e)

finally:
    driver.close()
