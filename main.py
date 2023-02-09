from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from keys import CHROME_BINARY_LOC, CHROME_DRIVER_PATH, CHROME_PROFILE_PATH
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
import time


s=Service(executable_path=CHROME_DRIVER_PATH)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")
chrome_options.binary_location=(CHROME_BINARY_LOC)
driver = webdriver.Chrome(service=s, options=chrome_options)


driver.get("https://www.asos.com/")

# Find the search bar element and enter a search term
search_bar = driver.find_element(By.CSS_SELECTOR,"input[data-testid='search-input']")
search_bar.send_keys("sweat pants")
search_bar.submit()

# Wait for the page to load
driver.implicitly_wait(10)

# Find all the product elements on the page
products = driver.find_elements(By.CLASS_NAME,"productTile_U0clN")

# Extract information from each product
for product in products:
    name = product.find_element(By.CSS_SELECTOR,"h2").text
    price = product.find_element(By.CSS_SELECTOR,"span").text
    print(f"Name: {name}, Price: {price}")

driver.quit()
