from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")






def login_to_chatgpt():
    try:
        # Initialize the Web Driver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # Start browser maximized (optional)
        # Uncomment below for headless mode (no UI)
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")

        # Initialize WebDriver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        driver.get("https://chat.openai.com/")
        print("opening ChatGPT")

        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))
        # ).click()
        # print("Clicked Log in.")









    except Exception as e:
       print(f"An error occured: {e}")
    finally:
        time.sleep(100)
        # driver.quit()

