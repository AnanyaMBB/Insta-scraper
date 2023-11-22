from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from seleniumwire.utils import decode
import time
import json

# ... [Your other imports here]

username = "besufekadananya@gmail.com"
password = "xc@12#@r"

url = "https://www.instagram.com/"
driver = webdriver.Chrome()

count = 0  # Keep track of processed requests count

def interceptor(request):
    global count  # Access the global count variable
    
    if request.response and request.url == 'https://www.instagram.com/api/graphql':
        body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity')).decode('utf-8')
        body = json.loads(body)
        
        if 'xdt_api__v1__clips__home__connection_v2' in body.get('data', {}).keys():
            with open(f'./dataset/unparsed_json/{count}.json', 'w', encoding='utf-8') as file:
                file.write(json.dumps(body, indent=4, ensure_ascii=False))
                print('Wrote to file')
            count += 1

# Assign the interceptor function to the driver
driver.request_interceptor = interceptor
# driver.response_interceptor = interceptor

try:
    driver.get(url)
    time.sleep(2)
    
    # [Your login steps here]
    username_field = driver.find_element("name", "username")
    username_field.send_keys(username)
    password_field = driver.find_element("name", "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(4)

    reels_url = "https://www.instagram.com/reels/"
    driver.get(reels_url)
    
    actions = ActionChains(driver)

    for _ in range(100000):
        time.sleep(2)
        actions.send_keys(Keys.PAGE_DOWN).perform()

finally:
    driver.quit()
