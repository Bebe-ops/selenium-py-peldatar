# A program segítségével olvasd be a csv tartalmat (table_in.csv). A feladatod, hogy az oldalon található
# formanyomtatvány segítségével feltöltsd a táblázatot. Használd a Python CSV könyvtárát.
# A feltöltött táblázatot ellenőrizheted ha a probramod letölti a táblázat alatti gomb segítségével az aktuális
# tartalmat. Hasonlítsd össze python kódból a kapott file-t, hogy identikus-e az eredetivel.

import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless
driver = webdriver.Chrome(ChromeDriverManager().install())


def find_and_clear_by_id(my_id):
    element = driver.find_element_by_id(my_id)
    element.clear()
    return element


try:
    driver.get("http://localhost:9999/another_form.html")

    with open("table_in.csv", encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        for row in reader:
            print(row)
            find_and_clear_by_id("fullname").send_keys(row[0])
            find_and_clear_by_id("email").send_keys(row[1])
            find_and_clear_by_id("dob").send_keys(row[2])
            find_and_clear_by_id("phone").send_keys(row[3])
            driver.find_element_by_id("submit").click()

    time.sleep(2)
    check_button = driver.find_element_by_xpath('//button[text()="Export HTML table to CSV file"]').click()
    time.sleep(2)

    # assert
    with open("table_in.csv", "r", encoding="utf-8") as origin_csv_file:
        reader = csv.reader(origin_csv_file, delimiter=",")
        next(reader)
        with open("C:\\Users\\anima\\Downloads\\table.csv", "r", encoding="UTF-8") as downloaded_file:
            csv_reader = csv.reader(downloaded_file, delimiter=",")
            next(csv_reader)
            for or_row, d_row in zip(reader, csv_reader):
                assert(or_row == d_row)
            print("Az adatok egyeznek")
except Exception as e:
    print("Az adatok nem egyeznek", e)
finally:
    driver.close()
