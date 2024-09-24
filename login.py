from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_to_swag_labs(username, password):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    
    time.sleep(3)
    
    # Verify successful login by checking the page title or URL
    if "inventory" in driver.current_url:
        print("Login successful")
    else:
        print("Login failed")
    
    driver.quit()
