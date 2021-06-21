from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/todo.html")

inputs = driver.find_elements_by_xpath('//li/span')
for elem in inputs:
    print(elem.text)

driver.close()
