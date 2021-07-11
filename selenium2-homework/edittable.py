# a) Adj hozzá még két teljesen kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok.
# b) Ellenőrizd a kereső funkciót.
# c) írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless
driver = webdriver.Chrome(ChromeDriverManager().install())


try:
    # tesztadatok az új sorokhoz
    data = ["lamp", "2.99", "3", "Home"]
    data2 = ["beer", "3.87", "10", "Joy"]

    driver.get("http://localhost:9999/editable-table.html ")
    add_btn = driver.find_element_by_xpath('//button[@class="btn btn-success pull-right"]')
    # meglévő sorok száma az eredeti táblázatban
    table_rows_num = len(driver.find_elements_by_xpath('//table[@class="table table-bordered"]/tbody/tr'))

    def fill_in_new_row(my_list):  # új sorok hozzáadása feladat/a)
        # létező sorok száma
        count_of_table_rows = len(driver.find_elements_by_xpath('//table[@class="table table-bordered"]/tbody/tr'))
        add_btn.click()
        time.sleep(1)
        cells = driver.find_elements_by_xpath(f'//table[@class="table table-bordered"]/tbody/tr[{count_of_table_rows}+1]/td/input')
        for i in range(len(my_list)):
            cells[i].clear()
            cells[i].send_keys(my_list[i])


    fill_in_new_row(data)
    time.sleep(1)
    fill_in_new_row(data2)

    # assert added rows
    added_rows = 2
    assert(table_rows_num + added_rows == len(driver.find_elements_by_xpath('//table[@class="table table-bordered"]/tbody/tr')))
    print("A sorok sikeresen hozzáadva.")

    # módosítás  feladat/c)
    # tesztadatok a módosításhoz
    test_cell_data = "Funs"
    test_cell_xpath = '//table[@class="table table-bordered"]/tbody/tr[3]/td[4]/input'
    test_cell = driver.find_element_by_xpath('//table[@class="table table-bordered"]/tbody/tr[3]/td[4]/input')

    def modified_cells(my_xpath, my_text):
        element = driver.find_element_by_xpath(my_xpath)
        element.clear()
        element.send_keys(my_text)
        return element


    modified_cells(test_cell_xpath, test_cell_data)

    # assert modified cell
    assert test_cell_data == test_cell.get_attribute("value")
    print("A módosítás sikeres.")

    # assert search function    feladat/b)
    # tesztadatok a search funkció ellenőrzéséhez
    test_text = data[0]
    search_field = driver.find_element_by_xpath('//input[@ placeholder = "Search..."]')

    def check_search(field, my_text):
        field.send_keys(my_text)
        assert field.get_attribute("value") == my_text
        print("A search funkció működik.")


    check_search(search_field, test_text)
except Exception as e:
    print("Sikertelen sor hozzáadás.", e)
    print("A módosítás sikertelen.", e)
    print("A search funkció nem működik", e)
finally:
    pass
    # driver.close()
