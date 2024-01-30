import time

import requests
import json

# Get data from FCA
headers = {
    "X-Auth-Key": "apikey",
    "X-Auth-Email": "email"
}

response = requests.get('https://register.fca.org.uk/services/V0.1/Search?q=Essex%20car%20company&type=Companies', headers=headers)

json_data = response.text
json_object = json.loads(json_data)
json_formatted_str = json.dumps(json_object, indent=2)
print(json_formatted_str)

# get data from ico

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service, Options
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless=False")
chrome_options.add_experimental_option("detach", True)
chrome_web_driver = Service(r"C:\Users\green\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_web_driver)
driver.maximize_window()
PROMISED_DOWN = 100
PROMISED_UP = 10
driver.get("https://ico.org.uk/ESDWebPages/Search")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'button[id="ccc-reject-settings"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'input[id="fieldname"]').send_keys("Essex car company")
driver.find_element(By.CSS_SELECTOR, 'input[type="image"]').click()
time.sleep(1)
main = driver.find_element(By.CSS_SELECTOR, 'main[id="main"]').find_elements(By.TAG_NAME, 'a')
print(main)
for hit in main:
    # print(hit.text)
    hit.click()
    time.sleep(2)
    label = driver.find_element(By.CSS_SELECTOR, 'dt[class="label"]')
    data = driver.find_element(By.TAG_NAME, 'dd')
    print(label.text, data.text)
    # driver.switch_to.new_window('tab')
    driver.back()
    time.sleep(10)

time.sleep(50)
