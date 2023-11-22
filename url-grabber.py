from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

# Replace these variables
username = "ananya.mb"
password = "bacdefhg"

url = "https://www.instagram.com/"

driver = webdriver.Chrome()

try:
    driver.get(url)
    time.sleep(2)  # wait for the page to load
    
    # Login
    username_field = driver.find_element("name", "username")
    username_field.send_keys(username)
    password_field = driver.find_element("name", "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(4)  # wait for login
    
    # Navigate to Reels
    reels_url = "https://www.instagram.com/reels/"
    driver.get(reels_url)
    time.sleep(2)  # wait for the page to load
    
    actions = ActionChains(driver)
    # Scroll and grab URLs
    urls = set()
    for _ in range(10):  # change the range value to scroll more or less

        current_url = driver.current_url  # get the current url from the address bar
        print(current_url)  # print the current url
        urls.add(current_url)
        # Scroll
        actions.send_keys(Keys.PAGE_DOWN).perform()
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # wait for more reels to load
    
    print(urls)
    
finally:
    driver.quit()
