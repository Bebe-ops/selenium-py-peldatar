# A célod, hogy ezeket (megadott) a dátum és idő értékeket(date01-06) selenium segítségével automatikusan beállítsd:
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, date, time, timezone
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless
driver = webdriver.Chrome(ChromeDriverManager().install())

now_utc = datetime.now(timezone.utc)
# test data
date01 = date(2021, 5, 6)
date02 = datetime(2012, 5, 5, 5, 5, 5, 555)  # megoldani, hogy ne írjon elé 000-át
date03 = datetime(2000, 12, 5, 12, 1)
date04 = date(1995, 12, 1)  # Kell egy nap is (elvárás 1995 december)
date05 = date(2015, 12, 28)  # dátum , 12.28 kb az 52 hét elvárás 52.hét bevitele)
date06 = datetime(2021, 12, 12, 12, 25)  # Kell az év, hó, nap az elejére (elvárás 12:25 óra-perc bevitele)

try:
    driver.get("http://localhost:9999/forms.html")
    date_field = driver.find_element_by_id("example-input-date")
    date_time_field = driver.find_element_by_id("example-input-date-time")
    date_time_local_field = driver.find_element_by_id("example-input-date-time-local")
    month_field = driver.find_element_by_id("example-input-month")
    week_field = driver.find_element_by_id("example-input-week")
    time_field = driver.find_element_by_id("example-input-time")

    # date field
    time.sleep(1)
    date_field.send_keys(date01.strftime('%Y\t%m%d'))  # kell a tab az év mező miatt ->6 karaktert fogad el a 4 helyett

    # date-time field
    time.sleep(1)
    date_time_field.send_keys(date02.strftime("%Y.%m.%d %H:%M:%S:%f").replace("000", ""))

    # date/Time local field
    time.sleep(1)
    date_time_local_field.send_keys(date03.strftime('%Y\t%m%d%I%M'))
    # date_time_local_field.send_keys(date03.strftime("%p"))  # PM-AM ide nem tudom bevinni

    # Month field
    time.sleep(1)
    month_field.send_keys(date04.strftime('%Y\t%B'))  # %B hónap stringben(december)

    # Week field
    time.sleep(1)
    week_field.send_keys(date05.strftime('%W'))
    week_field.send_keys(date05.strftime('%Y'))

    # # Time field
    time.sleep(1)
    time_field.send_keys(date06.strftime('%H'))
    time_field.send_keys(date06.strftime('%M'))
finally:
    driver.close()
