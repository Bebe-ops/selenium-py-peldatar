from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.get("https://pypi.org")


def my_searches():
    try:
        search = driver.find_element_by_id("search")
        search.send_keys("pip install selenium")
        submit = driver.find_element_by_class_name("search-form__button")
        submit.click()
        nem_letezo = driver.find_element_by_id("nemletezik")
    except NoSuchElementException:
        print(f'Nincs ilyen megjeleníthető elem.')


my_searches()
driver.close()
