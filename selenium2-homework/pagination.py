# Mentsd le az összes kontaktot az oldalról akinek a keresztneve (First Name) A betűvel kezdődik.
# A kiválasztott kontaktok összes adatát mentsd le memóriába egy szótár (dict) struktúrába.
# Amikor megvagy az összes adatot mentsd ki egy CSV file-ba.
import csv

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pprint
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'http://localhost:9999/pagination.html'
extracted_data = []
try:
    driver.get(url)
    time.sleep(2)
    while True:
        table = driver.find_element_by_xpath('//table[@id="contacts-table"]/tbody')
        rows = table.find_elements_by_tag_name('tr')
        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name('td')
            data_row["id"] = cells[0].text
            data_row["first_name"] = cells[1].text
            data_row["second_name"] = cells[2].text
            data_row["surname"] = cells[3].text
            data_row["second_surname"] = cells[4].text
            data_row["birth_date"] = cells[5].text
            if cells[1].text.startswith('A'):
                extracted_data.append(data_row)
        next_button = driver.find_element_by_id('next')
        # vizsgálat: vannak e további oldalak (adat)
        if not next_button.is_enabled():
            break
        else:
            next_button.click()
    pprint.pprint(extracted_data)
    print(len(extracted_data))

    # save as csv.file
    with open("startswithA.csv", "w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(extracted_data)
finally:
    driver.close()
