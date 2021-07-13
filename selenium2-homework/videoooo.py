from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "http://localhost:9999/videos.html "

try:
    driver.get(url)

    # html5 player start/stop & screenshot
    html5_video_id = 'html5video'

    def html5_video_player(my_id):
        video_player = driver.find_element_by_id(my_id)
        video_player.send_keys(Keys.SPACE)
        time.sleep(10)
        video_player.send_keys(Keys.SPACE)
        video_player.screenshot('video_scr_shot1.png')

    html5_video_player(html5_video_id)

    # html5 player with custom controls start/stop & screenshot
    c_cont_video_xp = '//div/button[text()="Play/Pause"]'

    def custom_controls_player(my_xpath):
        video_player = driver.find_element_by_xpath(my_xpath)
        video_player.click()
        video_player.screenshot('video_src_shot2.png')
        time.sleep(5)
        video_player.click()

    custom_controls_player(c_cont_video_xp)

    # html5 player screen-size check
    time.sleep(2)
    big_expected_size = ["big", "560"]
    small_expected_size = ["small", "320"]
    normal_expected_size = ["normal", "420"]

    def size_btn_click(xp, size):
        driver.find_element_by_xpath(xp).click()
        video_screen_size = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'video1')))
        assert video_screen_size.get_attribute("width") == size
        print(f'{size} is the same as the actual result: {video_screen_size.get_attribute("width")}')
        time.sleep(2)

    size_btn_click('//div/button[text()="Big"]', big_expected_size[1])  # big_btn
    size_btn_click('//div/button[text()="Small"]', small_expected_size[1])  # small_btn
    size_btn_click('//div/button[text()="Normal"]', normal_expected_size[1])  # normal_btn

    # Big Buck Bunny link --> új ablak
    link = driver.find_element_by_xpath('//p/a[@target="_blank"]').click()
    main_window = driver.window_handles[0]
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    time.sleep(2)
    driver.close()
    driver.switch_to.window(main_window)

    # Embedded youtube video in iframe (beágyazott)
    iframe = driver.find_element_by_id('youtubeframe')
    driver.switch_to.frame(iframe)
    play = driver.find_element_by_id('player')
    play.click()
    time.sleep(5)
    play.click()
    play.screenshot('video_youtube_scr_shot.png')
finally:
    driver.close()
