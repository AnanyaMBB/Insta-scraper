# from instascrape import Reel
# import time

# # pip install instascrape

# # This code will download the reel for sure, but not if you continue to make the request again and again, and hence, you need to pass the session id. Recently, due to updated policies of Instagram, it is not that easy to scrape it. Hence with the above code, we need to pass the session id into the headers as follows:

# SESSIONID = "18abbab1359-409ef7"
# # SessionID changes every time when you log out. Make sure that you provide the id at the time when you are logged in.

# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
# "cookie":f'sessionid={SESSIONID};'
# }
# #test@123
# google_reel=Reel('https://www.instagram.com/reels/CxJlgCxBubP/')
# google_reel.scrape(headers=headers)

# # fstring Format = convenient way to embed python expressions inside string literals for formatting. 
# google_reel.download(fp=f".//reel{int(time.time())}.mp4")
# print('Downloaded Successfully.')



# # from instascrape import Reel
# # import time
 
# # # session id
# # SESSIONID = "18abbab1359-409ef7"
 
# # # Header with session id
# # headers = {
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
# #     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
# #     Safari/537.36 Edg/79.0.309.43",
# #     "cookie": f'sessionid={SESSIONID};'
# # }
 
# # # Passing Instagram reel link as argument in Reel Module
# # insta_reel = Reel(
# #     'https://www.instagram.com/reels/CxJlgCxBubP/')
 
# # # Using  scrape function and passing the headers
# # insta_reel.scrape(headers=headers)
 
# # # Giving path where we want to download reel to the
# # # download function
# # insta_reel.download(fp=f".\\Desktop\\reel{int(time.time())}.mp4")
 
# # # printing success Message
# # print('Downloaded Successfully.')

# # def download(url,params):
# #     import requests
# #     import re
# #     from requests_html import HTMLSession
# #     try:
# #         params=str(params)
# #         verify=re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",url)
# #     except:
# #         return ValueError("Invalid params!")
# #     if __name__ == '__main__':
# #         print(verify)
# #     if verify[0][0]==url:
# #         pass
# #     else:
# #         raise ValueError("Wrong url Supplied")
# #     try:

# #         session = HTMLSession()
# #         response = session.get(url).text
# #         final= re.findall(r'content="https://scontent-bom1-1.cdninstagram.com/v/(.*?)[\"\']',response)[-1]
# #         print('https://scontent-bom1-1.cdninstagram.com/v/'+final)
# #         # print(response)
# #         import requests
# #         r = requests.get('https://scontent-bom1-1.cdninstagram.com/v/'+final, stream=True)
# #         with open(params, "wb") as f:
# #             for c in r.iter_content(chunk_size=1024 * 1024):
# #                 if c:
# #                     f.write(c)
# #                     if __name__ == '__main__':
# #                         print("Done")


# #     except requests.exceptions.RequestException as e:
# #         raise str(e)
# # if __name__ == '__main__':
# #     download('https://www.instagram.com/reels/CxJlgCxBubP/','video.mp4')



import requests

url = "https://www.instagram.com/api/graphql"

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "dpr": "1",
    "pragma": "no-cache",
    "sec-ch-prefers-color-scheme": "dark",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
    "sec-ch-ua-full-version-list": "\"Microsoft Edge\";v=\"117.0.2045.36\", \"Not;A=Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"117.0.5938.89\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "viewport-width": "1012",
    "x-asbd-id": "129477",
    "x-csrftoken": "sFc9FFOzDbNl9ZbWPDss38bC81jvM9ZN",
    "x-fb-friendly-name": "PolarisClipsTabDesktopContainerQuery",
    "x-fb-lsd": "CmW5rXcJxlnST4Fb3IJRBm",
    "x-ig-app-id": "936619743392459"
}

data = "v=17841437890617318&__d=www&__user=0&__a=1&__req=m&__hs=19622.HYP%3Ainstagram_web_pkg.2.1..0.1&dpr=1&__ccg=UNKNOWN&__rev=1008797135&__s=ky4l5v%3Ah19xai%3Afw3vlj&__hsi=7281557979237958874&__dyn=7xeUmwlEnwn8K2WnFw9-2i5U4e0yoW3q32360CEbo1nEhw2nVE4W0om78b87C0yE7i0n24o5-1ywOwv89k2C1Fwc60D8vw8O4U2zxe2GewGwso88cobEaU2eU5O3y1Sx_w4HwJCwLyESE7i3u2C2O0z8c86-3u361pg661pwr86C1mwraCg&__csr=gaL8D6hbdh1YjSPZOhREK-88HiHGFHKm8VrBKFk10ueUzD-UZ5zUrnVoCfgCUpGbCgG2CEjxq9xe00hBh05Q500wbw2gS350hN0kBwc3c13DxO0dfwyoG0wA1Jw7gw2zU0TUw04X-8w&__comet_req=7&fb_dtsg=NAcNiXGng9x8ZodR-6NZU_aG1xeoCEG8qyPmuO2v0xCh3JZ8SKfpEcA%3A17853667720085245%3A1695369828&jazoest=26219&lsd=CmW5rXcJxlnST4Fb3IJRBm&__spin_r=1008797135&__spin_b=trunk&__spin_t=1695369831&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PolarisClipsTabDesktopContainerQuery&variables=%7B%22data%22%3A%7B%22container_module%22%3A%22clips_tab_desktop_page%22%7D%7D&server_timestamps=true&doc_id=24690270033905252"

response = requests.post(url, headers=headers, data=data)

# Check the status code and the response (if needed)
print(response.status_code)
print(response.text)
