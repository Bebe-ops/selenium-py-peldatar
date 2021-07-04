from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless
driver = webdriver.Chrome(ChromeDriverManager().install())
try:
    driver.get("http://localhost:9999/todo.html")
    inputs = driver.find_elements_by_xpath('//li/span[@class="done-false"]')
    for elem in inputs:
        print('Todo:', elem.text)
except NoSuchElementException as e:
    print("Element not found", e)
finally:
    driver.close()
