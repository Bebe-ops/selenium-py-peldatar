# A program töltse be a példatárból az http://localhost:9999/loadmore.html oldalt.
# Mentsd le az első 20 macskás képet az oldalról.
# A fájlokat egy külön cats könyvtárba mentsd le.
# A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük, hogy hányadiknak lett megjelenítve
# és cat_id meg az azonosító amit szolgáltató ad. A {} jelek ne legyenek benne a fájlnévben.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import requests
import os

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless


# mappa létrehozása
os.makedirs(
    "C:\\Users\\anima\\PycharmProjects\\hazi_feladatok_minta_megoldasok\\selenium2_homeworks\\cats", exist_ok=True)

try:
    url = "http://localhost:9999/loadmore.html"
    driver.get(url)
    time.sleep(3)
    load_more_btn = driver.find_element_by_tag_name('button')

    for _ in range(3):
        load_more_btn.click()

    time.sleep(5)
    divs = driver.find_elements_by_xpath('//div[@class="image"]')
    for index, elem in enumerate(divs):
        cat_img = driver.find_element_by_tag_name('img')
        cat_url = cat_img.get_attribute('src')
        cat_id = elem.find_element_by_tag_name('p').text.replace("Cat id: ", "")
        file_name = f'{index}_{cat_id}'
        # print(file_name, cat_id)  # check

        r = requests.get(cat_url)  # request.get()  -> HTTP kérésre elkérem a választ
        if r.status_code == 200:
            with open(f'C:\\Users\\anima\\PycharmProjects\\hazi_feladatok_minta_megoldasok\\selenium2_homeworks\\cats\\{file_name}', "wb") as file:
                file.write(r.content)
finally:
    pass
driver.close()
