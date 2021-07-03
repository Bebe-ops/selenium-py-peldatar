from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless mód
driver = webdriver.Chrome(ChromeDriverManager().install())


def find_elem_by_id(my_id):
    element = driver.find_element_by_id(my_id)
    return element


try:
    driver.get("http://localhost:9999/trickyelements.html")
    find_elem_by_id("randomized")
    find_elem_by_id("difficulty")
    find_elem_by_id("element1")
    find_elem_by_id("element2")
    find_elem_by_id("element3")
    find_elem_by_id("element4")
    find_elem_by_id("element5")
    first_button = driver.find_element_by_xpath("/html/body/form/button[1]")
    first_button.click()
    result = driver.find_element_by_id("result")
    print(result.text)
    assert(result.text == f'{first_button.text} was clicked')
    print("Test finished OK!")

except NoSuchElementException as e:
    print('Element not found: ', e)

finally:
    driver.close()
