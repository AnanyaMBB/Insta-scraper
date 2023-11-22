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


# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('processed_data.db')

# Create a cursor object using the connection
cur = conn.cursor()

# Create tables for processed_hashes and processed_requests if they don't exist
cur.execute('''CREATE TABLE IF NOT EXISTS processed_hashes
               (hash TEXT PRIMARY KEY)''')

cur.execute('''CREATE TABLE IF NOT EXISTS processed_requests
               (url TEXT PRIMARY KEY)''')

conn.commit()



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
    for _ in range(100000):
        time.sleep(2)
        for request in driver.requests:
            if request.response is not None:
                cur.execute('SELECT url FROM processed_requests WHERE url = ?', (request.url,))
                
                if cur.fetchone() is not None:
                    print("Request already processed")
                    continue
                
                if request.url == 'https://www.instagram.com/api/graphql':
                    body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity')).decode('utf-8')
                    
                    
                    # Compute the MD5 hash of the body
                    body_hash = md5(body.encode('utf-8')).hexdigest()
                    
                    # Check if this hash has already been processed
                    # cur.execute(f'SELECT hash FROM processed_hashes WHERE hash = {body_hash}')
                    # if cur.fetchone() is not None:
                    #     print("Hash already processed")
                    #     continue

                    body = json.loads(body)
                    if 'xdt_api__v1__clips__home__connection_v2' in body['data'].keys():
                    
                        # Write the body to the file as it is not a duplicate
                        with open(f'./dataset/unparsed_json/{count}.json', 'w', encoding='utf-8') as file:
                            file.write(json.dumps(body, indent=4, ensure_ascii=False))
                        print("Saved file")
                        # Add the hash of this body to the set of processed hashes
                        cur.execute('INSERT INTO processed_hashes (hash) VALUES (?)', (body_hash,))
                        conn.commit()
                        # processed_hashes.add(body_hash)
                        count += 1

            cur.execute('INSERT OR IGNORE INTO processed_requests (url) VALUES (?)', (request.url,))
  
            conn.commit()  
            # processed_requests.add(request)
        print("Button Pressed")
        actions.send_keys(Keys.PAGE_DOWN).perform()
        

finally:
    driver.quit()