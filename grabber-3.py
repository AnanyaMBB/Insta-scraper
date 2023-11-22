from seleniumwire import webdriver
import time
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import brotli

# Keep the username, password confidential and do not expose them in the code
username = "ananya.mb"
password = "bacdefhg"

url = "https://www.instagram.com/"
driver = webdriver.Chrome()

try:
    driver.get(url)
    time.sleep(2)
    
    # Login
    username_field = driver.find_element("name", "username")
    username_field.send_keys(username)
    password_field = driver.find_element("name", "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(4)
    
    # Navigate to Reels
    reels_url = "https://www.instagram.com/reels/"
    driver.get(reels_url)
    driver.get(reels_url)

    actions = ActionChains(driver)
    processed_request_bodies = set()  # To keep track of processed request bodies
    count = 0

    for _ in range(40):  
        time.sleep(4)

        for request in driver.requests:
            if request.method == 'POST' and 'https://www.instagram.com/api/graphql/' in request.url:
                content_encoding = request.response.headers.get('Content-Encoding', 'identity')
                body = request.response.body
                body = brotli.decompress(body)
                
                if body not in processed_request_bodies:  # Check uniqueness of the body
                    try:
                        j = json.loads(body)  # try to parse the body as json
                        
                        # Check if the response body contains required keys
                        if any(key in body for key in ['feed', 'clips', 'clip']):
                            with open(f'output{count}.json', 'a', encoding='utf-8') as f:
                                f.writelines(json.dumps(j, indent=4, ensure_ascii=False))
                                count += 1
                                processed_request_bodies.add(body)
                    except json.JSONDecodeError as e:
                        print(f"Failed to decode JSON: {e}")

        driver.requests.clear()
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
    
finally:
    driver.quit()