from seleniumwire import webdriver
from seleniumwire.utils import decode
import time
import zlib
import brotli
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json

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
    
    
    actions = ActionChains(driver)
    urls = set()
    count = 0
    for _ in range(40):  # change the range value to scroll more or less
        time.sleep(4)
    
        for request in driver.requests:
            # print("Resuest ", request)
            if request.method == 'POST' and 'https://www.instagram.com/api/graphql/' in request.url:
                content_encoding = request.response.headers.get('Content-Encoding', 'identity')
                body = request.response.body
                    
                if content_encoding == 'gzip':
                    body = zlib.decompress(body, zlib.MAX_WBITS|32)
                elif content_encoding == 'deflate':
                    body = zlib.decompress(body)
                elif content_encoding == 'br':
                    body = brotli.decompress(body)
                        
                content_type = request.response.headers.get('Content-Type', '')
                if 'text' in content_type or 'json' in content_type:
                    try:
                        body = body.decode('utf-8')
                        j = json.loads(body)  # try to parse the body as json
                        
                        # Check if the response body contains "xdt_api__v1__feed__timeline__connection"
                        if 'feed' in body or 'clips' in body or 'clip' in body:
                            with open(f'output{count}.json', 'a', encoding='utf-8') as f:
                                f.writelines(json.dumps(j, indent=4, ensure_ascii=False))
                                count+=1
                    except UnicodeDecodeError as e:
                        with open('output.txt', 'a', encoding='utf-8') as f:
                            f.writelines('Failed to decode response body: ' + str(e))
        driver.requests.clear()
            # time.sleep(2)
        current_url = driver.current_url
        print(current_url)
        urls.add(current_url)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
    
    print(urls)
    
finally:
    driver.quit()
