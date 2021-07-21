# A feladatod, hogy megtaláld a random kiválasztott színhez tartozó gombot.
# Ha egy gombra rákattintasz az egy új ablakot fog feldobni, egy valamilyen színben tündököl.
# Ügyelj arra, hogy ne árassza el a képernyődet a sok ablak.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    url = "http://localhost:9999/windowgame.html"
    driver.get(url)
    time.sleep(3)

    target_color = driver.find_element_by_xpath('//p[@id="target_color"]').text
    print(f'Target color: {target_color}')

    all_btn = driver.find_elements_by_tag_name('button')
    main_win = driver.window_handles[0]
    for _ in all_btn:
        _.click()
        color_win = driver.window_handles[1]
        driver.switch_to.window(color_win)
        color_h1 = driver.find_element_by_xpath('//h1').text
        driver.close()
        driver.switch_to.window(main_win)
        if target_color != color_h1:
            pass
        else:
            num_of_guesses = driver.find_element_by_id('numberOfGuesses').text
            print(f"You win!. Number of guesses made: {num_of_guesses}")
            break
finally:
    pass
# driver.close()






