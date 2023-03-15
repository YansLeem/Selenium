from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.service import Service
import os
from time import sleep


Driver_path = os.getcwd() + r"\chromedriver.exe"
#service = Service("C:/Users/RU20028465/Desktop/Python/Hello_World/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument('--headless')
#global driver
driver = webdriver.Chrome(executable_path=Driver_path, chrome_options=options)
driver.get("https://dzen.ru/")
sleep(3)
Element = driver.find_element_by_xpath( "/html/body/div[2]/div[2]/div[4]/main/section[2]/div[2]/div/a[2]")
sleep(3)
Element.click()
sleep(3)
driver.get_screenshot_as_file("Screen.png")
