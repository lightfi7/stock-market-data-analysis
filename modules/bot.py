import os
from selenium import webdriver
from selenium.webdriver.common.by import By

username = os.environ['OO_USERNAME']
password = os.environ['OO_PASSWORD']

print(username)
print(password)

browser = webdriver.Chrome()

# Start Login
browser.get('https://optionomega.com/login')

browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[1]/input').send_keys(username)
browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[2]/input').send_keys(password)
browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[4]/button').click()
# End Login

# Start Backtest


# End Backtest



