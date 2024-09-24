def add_and_remove_item(username, password):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    # Login steps
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    
    # Add item to cart
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "1", "Item not added to cart"
    
    # Remove item from cart
    driver.find_element(By.CLASS_NAME, "btn_secondary").click()
    time.sleep(2)
    assert not driver.find_elements(By.CLASS_NAME, "shopping_cart_badge"), "Item not removed from cart"
    
    driver.quit()
