# Nyisson meg egy Chrome böngészőt és töltsön be egy tetszőleges weblapot az Internetről.
# Az oldalon próbáld megtalálni a <div id="nemletezik"></div> mezőt.
# A lényeg, hogy hibát dobjon a driver.find_by_id függvény hívás.
# Feladatot, hogy kezed le ezt a hibát és írj ki valami emberileg olvasható üzenetet.

# Extra feladatként készíts egy saját függvényt, ami bármilyen find_by_id lokátor hívásnál lekezeli a nemlétező
# elem tipusú hibát.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://pypi.org")


def my_searches():
    try:
        search = driver.find_element_by_id("search")
        search.send_keys("pip install selenium")
        submit = driver.find_element_by_class_name("search-form__button")
        submit.click()
        nem_letezo = driver.find_element_by_id("nemletezik")
    except NoSuchElementException as e:
        print(f'Element not found', e)
    finally:
        driver.close()


my_searches()



# # extra feladat
# def exception(my_id):
#     try:
#         driver.get("https://pypi.org")
#         elements = driver.find_element_by_id(my_id)
#     except NoSuchElementException as e:
#         print(f'Element not found', e)
#     finally:
#         driver.close()
#
#
# exception("nemletezik")
