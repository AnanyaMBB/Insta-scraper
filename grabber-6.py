import concurrent.futures
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
# ... [Other Imports] ...

def process_request(request):
    if request.response is not None:
        if request.url == 'https://www.instagram.com/api/graphql':
            body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity')).decode('utf-8')
            
            body = json.loads(body)
            if 'xdt_api__v1__clips__home__connection_v2' in body['data'].keys():
                with open(f'./dataset/unparsed_json/{count}.json', 'w', encoding='utf-8') as file:
                    file.write(json.dumps(body, indent=4, ensure_ascii=False))
                
                # Here count needs to be properly synchronized between threads.
                # For simplicity it is not synchronized in this snippet
                # as this is just to give you an idea of how to use threading
                count += 1


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

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(100000):
            time.sleep(2)
            length = len(driver.requests)
            
            futures = [executor.submit(process_request, driver.requests[i]) for i in range(i, length)]
            concurrent.futures.wait(futures)

            actions.send_keys(Keys.PAGE_DOWN).perform()
            print("Button Pressed")

finally:
    driver.quit()
