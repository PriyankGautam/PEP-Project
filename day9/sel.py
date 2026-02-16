from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/login")

time.sleep(6)

username = driver.find_element(By.ID, "username")
username.send_keys("admin")
password = driver.find_element(By.ID, "password")
password.send_keys("admin")
login_button = driver.find_element(By.CSS_SELECTOR , "input[type='submit']")
login_button.click()


time.sleep(6)
driver.quit()