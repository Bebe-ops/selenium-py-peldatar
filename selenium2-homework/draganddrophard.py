# A feladatod, hogy a to-do oszlopból átrakd az összes kártyát a doing oszlopba.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from os import getcwd

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless

try:
    driver.maximize_window()
    driver.get("http://localhost:9999/dragndrop2.html")
    time.sleep(2)
    cwd = getcwd()
    JS_DRAG_AND_DROP = open(cwd + '\\drag_and_drop_helper.js', 'r').read()  # beolvasom a lementett JS kódot

    target = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, '//div[@class="inner"]/ul[@id="Doing"]')))


    def drag_and_drop(xp):
        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xp)))
        driver.execute_script(JS_DRAG_AND_DROP, element, target)
        driver.implicitly_wait(5)


    drag_and_drop('//div[@class="inner"]/ul/li[@id="Pizza"]')
    drag_and_drop('//div[@class="inner"]/ul/li[@id="Tacos"]')
    drag_and_drop('//div[@class="inner"]/ul/li[@id="BBQ"]')
    drag_and_drop('//div[@class="inner"]/ul/li[@id="Burgers"]')

finally:
    driver.close()
