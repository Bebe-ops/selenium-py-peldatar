from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://nasa.gov")

q = driver.find_element_by_name("query")
q.send_keys("ingenuity")

# submit = driver.find_element_by_id("ember30")
submit = driver.find_element_by_xpath('//input[@id="ember30"]')
submit.click()

contact = driver.find_element_by_link_text("Contact NASA")
contact.click()

driver.close()
