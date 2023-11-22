from seleniumwire import webdriver
from seleniumwire.utils import decode
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
import brotli
from hashlib import md5
import sqlite3
from collections import deque

# username = "ananya.mb"
# password = "bacdefhg"
username = "besufekadananya@gmail.com"
password = "xc@12#@r"

url="https://www.instagram.com/"
driver = webdriver.Chrome()


try:
    
    driver.get(url)
    time.sleep(2)

    username_field = driver.find_element("name", "username")
    username_field.send_keys(username)
    password_field = driver.find_element("name", "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    time.sleep(4)

    driver.requests.clear()
    reels_url = "https://www.instagram.com/reels/"
    driver.get(reels_url)

    actions = ActionChains(driver)
    processed_requests = set()
    processed_hashes = set()

    count = 0
    i = 0
    for _ in range(100000):
        time.sleep(2)
        for idx in range(i, len(driver.requests)):
            request = driver.requests[idx]
            print(idx)
            if request.response is not None:
                if request.url == 'https://www.instagram.com/api/graphql':
                    body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity')).decode('utf-8')
                    print('Found graphql request')
                    
                    body = json.loads(body)
                    print(body['data'].keys())
                    if 'xdt_api__v1__clips__home__connection_v2' in body['data'].keys():
                        print('Found reels request')
                        # Write the body to the file as it is not a duplicate
                        with open(f'./dataset/unparsed_json/{count}.json', 'w', encoding='utf-8') as file:
                            file.write(json.dumps(body, indent=4, ensure_ascii=False))
                            print('Wrote to file')
                        # Add the hash of this body to the set of processed hashes
                        # processed_hashes.add(body_hash)
                        count += 1
            i += 1
                
            # processed_requests.add(request)
        
        actions.send_keys(Keys.PAGE_DOWN).perform()
        
        

finally:
    driver.quit()