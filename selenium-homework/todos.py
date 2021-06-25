from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/todo.html")

inputs = driver.find_elements_by_xpath('//li/span')
for elem in inputs:
    print(elem.text)

driver.close()
