# még nincs meg a switch tudás. Majd visszatérek
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())


try:
    driver.get("http://localhost:9999/general.html")
    links = driver.find_elements_by_xpath('//a[starts-with(@href,"#")]')
    for r in links:
        if r.text == '#':
            links.remove(r)

    for i in links:
        if i.get_attribute("target"):
            continue
        else:
            i.click()
            time.sleep(1.0)
            print(driver.current_url)
            driver.back()
except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()
