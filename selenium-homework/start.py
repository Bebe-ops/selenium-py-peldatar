from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://nasa.gov")

q = driver.find_element_by_name("query")
q.send_keys("ingenuity")
q.send_keys(Keys.ENTER)

contact = driver.find_element_by_link_text("Contact NASA")
contact.click()

driver.close()
