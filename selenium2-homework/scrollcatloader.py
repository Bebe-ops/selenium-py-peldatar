# Mentsd le az első 20 macskás képet az oldalról. A fájlokat egy külön cats könyvtárba mentsd le.
# A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük, hogy hányadiknak lett megjelenítve
# és cat_id meg az azonosító amit szolgáltató ad. A {} jelek ne legyenek benne a fájlnévben.
# (ez a feladat majdnem ugyan az, mint az előző feladat, csakhogy nincs load more gomb.)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    "C:\\Users\\anima\\PycharmProjects\\hazi_feladatok_minta_megoldasok\\selenium2_homeworks\\cats2", exist_ok=True)

try:
    url = 'http://localhost:9999/scrolltoload.html '
    driver.get(url)
    time.sleep(5)

    js = "window.scrollTo(0, document.body.scrollHeight);"
    img_number = 20
    divs = []

    while len(divs) < img_number:
        divs = WebDriverWait(driver, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="image"]')))
        driver.execute_script(js)
        time.sleep(5)

    assert len(divs) == 20

    for index, div in enumerate(divs):
        cat_img = div.find_element_by_tag_name("img")
        cat_url = cat_img.get_attribute("src")
        cat_id = div.find_element_by_tag_name('p').text.replace("Cat id: ", "")
        file_name = f'{index}_{cat_id}'
        print(index, cat_id)

        r = requests.get(cat_url)
        if r.status_code == 200:
            with open(f'C:\\Users\\anima\\PycharmProjects\\hazi_feladatok_minta_megoldasok\\selenium2_homeworks\\'
                      f'cats2\\{file_name}', "wb") as file:
                file.write(r.content)
finally:
    pass
    driver.close()
