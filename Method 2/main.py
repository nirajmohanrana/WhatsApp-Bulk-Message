from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

from urllib.parse import quote
import time

# Variables
msg = ""
numbers = []
whatsAppLink = "https://web.whatsapp.com"

# READING MESSAGE
with open('Method 2/message.txt', 'r') as msgFile:
    msg = quote(msgFile.read())

#READING NUMBERS
with open('Method 2/numbers.txt', 'r') as numFile:
    for num in numFile.readlines():
        numbers.append(num.rstrip())

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(whatsAppLink)
time.sleep(30)

for num in numbers:
    sendMessageLink = f'{whatsAppLink}/send/?phone={num}&text={msg}'
    driver.get(sendMessageLink)

    time.sleep(10)

    action = ActionChains(driver)
    action.send_keys(Keys.CONTROL+ "v")
    action.send_keys(Keys.ENTER)
    action.perform()

    time.sleep(10)

time.sleep(2000)
