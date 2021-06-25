from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless
# driver = webdriver.Chrome(ChromeDriverManager().install())

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
