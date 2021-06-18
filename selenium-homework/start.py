from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://nasa.gov")

q = driver.find_element_by_name("query")
q.send_keys("ingenuity")

submit = driver.find_element_by_id("ember23")
submit.click()

contact = driver.find_element_by_link_text("Contact NASA")
contact.click()

driver.close()
