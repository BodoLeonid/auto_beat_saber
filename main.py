import os
import selenium
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unpack import unpack
from config import *


songs_folder = os.path.abspath("songs")
upload_url = URL_PATH
flag = False


try:
    driver = webdriver.Chrome()
except selenium.common.exceptions.SessionNotCreatedException:
    print(
        "Could not create a session: You must enable 'Allow remote automation' in the Developer section of Safari Settings to control Safari via WebDriver"
    )


for filename in os.listdir(songs_folder):
    if filename.endswith(".mp3"):
        file_path = os.path.join(songs_folder, filename)

        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])

        driver.get(upload_url)

        upload_input = driver.find_element(By.XPATH, "//input[@type='file']")

        upload_input.send_keys(file_path)

        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                label = checkbox.find_element(By.XPATH, "./following-sibling::span")
                label.click()

        yellow_cube = driver.find_element(By.ID, "bottom")
        yellow_cube.click()

        if not flag:
            for i in range(2):
                yellow_cube.click()
            flag = True


input(
    "Дождитесь загрузки всех файлов, после чего нажмите Enter, чтобы закрыть браузер..."
)

driver.quit()

need_to_upack_guess = False
if not NEED_TO_UNPACK:
    need_to_upack_guess = (
        input(
            "Распаковать скачанные архивы в папку с игрой(нужно предварительно указать путь в config.py)? (y/n):  "
        ).strip()
        == "y"
    )

if NEED_TO_UNPACK or need_to_upack_guess == "y":
    unpack()
