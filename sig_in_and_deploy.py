from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Schedule_Script:

    def launch(self,):
        service =  Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get(url)
        driver.maximize_window()
        input("")

url = "https://kalaloka.com"

Schedule_Script.launch(url)
