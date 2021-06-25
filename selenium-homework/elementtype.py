from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless mód
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/trickyelements.html")

randomized = driver.find_element_by_id("randomized")
difficulty = driver.find_element_by_id("difficulty")
element1 = driver.find_element_by_id("element1")
element2 = driver.find_element_by_id("element2")
element3 = driver.find_element_by_id("element3")
element4 = driver.find_element_by_id("element4")
element5 = driver.find_element_by_id("element5")
result = driver.find_element_by_id("result")


def button_click():
    try:
        first_button = driver.find_element_by_xpath("/html/body/form/button[1]")
        first_button.click()
        print(result.text)
        assert(result.text == f'{first_button.text} was clicked')
    except NoSuchElementException:
        print("Nincs button típusú elem.")


button_click()

driver.close()
