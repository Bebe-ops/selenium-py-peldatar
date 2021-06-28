from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999")

links = [elem.get_attribute("href") for elem in driver.find_elements_by_tag_name('a')]


def get_all_links(driver):  # kiveszem a href attribútumokat
    links = []
    elements = driver.find_elements_by_tag_name('a')
    for elem in elements:
        href = elem.get_attribute("href")
        links.append(href)
    return links


print(len(links))

# fájlba írás soronként
with open('link_datas.txt', 'w') as out_file:
    out_file.write('\n'.join(links))

driver.close()