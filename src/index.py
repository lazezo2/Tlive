from fastapi import FastAPI

from src.dtos.ISayHelloDto import ISayHelloDto

from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests
import os
import re
#import urllib.parse
from fastapi.middleware.cors import CORSMiddleware

import unicodedata

rpctoken = os.environ["rpctoken"]

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/hello")
async def hello_message(dto: ISayHelloDto):
    return {"message": f"Hello {dto.message}"}

class qdata(BaseModel):
    user: int
    use_cookies: str
    Cookie: str
    
@app.post("/live")
async def live(data: qdata):
    user = data.user
    use_cookies = data.use_cookies
    Cookie = data.Cookie
    
    show_prints = 1
    
    if use_cookies == 0:
      device_id=7210654296430074269
    
    xxxxxx = 1    
    if xxxxxx == 1:        
      referer=f"https%3A%2F%2Fwww.tiktok.com%2F%40{user}"
      root_referer=f"https%3A%2F%2Fwww.tiktok.com%2F%40{user}"
      webcast_language = "en"
      user_is_login="true"
      uniqueId=user
      screen_width=1138
      screen_height=640
      region="EG"            
      priority_region="EG"
      os="windows"
      is_fullscreen="false"
      focus_state="false"
      data_collection_enabled="true"
      cookie_enabled="true"
      browser_version="5.0%20%28Windows%29"
      browser_platform="Win32"
      browser_name="Mozilla"
      browser_language="en-US"
      app_name="tiktok_web"
      device_platform="web_pc"
      msToken="5SCWCt7PGz_mOJFXwrLA-0r4f9hY2FZllCTPwAYNfiFJR6GwY7pfS0i3JN1oeKyhZkiKKImGRihhzDVaRBAwt0YS_Pl2cDBjFcTnkRa_lHWZbWCTxyaeirZpAgoM4e9bHEyeEsexjU310T2d8ZIHsYyrow==&"
      xbogus="DFSzsIVu8ZhANyg-COFo78a6TzRh"
      XGnarly="M/9P0p9v7NNkdAgd3LfiU5omxrMlwz2Gea7EryeZy8BEti-1J7I2U4t25XUtE6H3A4iVoJfP3UBNI-PUWN7L2v-Y76b4b0Ix8E0ZD5ygsLnEfw5FIKpshsPyJjcRaMG6xRBFDOwHiCaDIHrqvStSoAzSdiV6cbI0yb-BkMXci3ijZwWEqNleaEBxgcb7L21dmVmWjFTMxwU1BGtWVP5obShmfdaXUh1hRqEvxbmC06p80lj3JSsZtG-XSlIEoPS-EJBKzBLBmoVXj/TubNc5juP4J66RDsaXtK7Oqin3ei78WRrwapXoprTcK9b7fjUhjDn="
      sourceType=54

      headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Referer": f"https://www.tiktok.com/@{uniqueId}/live",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Connection": "keep-alive",
                "Priority": "u=4",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache"
      }
      if use_cookies == 1:
         headers["Cookie"] = Cookie
    
      """
      get xGnarly
      """
      #####
      url_xGnarly = "https://xgnray.vercel.app/api/xgnarly"  # استبدلها برابط API الحقيقي
      # removed verify_fp
      data_xGnarly = {
                #"queryString": f"aid=1988&app_language=en&app_name={app_name}&browser_language={browser_language}&browser_name={browser_name}&browser_online=true&browser_platform={browser_platform}&browser_version={browser_version}&channel=tiktok_web&cookie_enabled={cookie_enabled}&data_collection_enabled={data_collection_enabled}&device_id={device_id}&device_platform={device_platform}&focus_state={focus_state}&from_page=&history_len=6&is_fullscreen={is_fullscreen}&is_page_visible=true&os={os}&priority_region={priority_region}&referer={referer}&region={region}&root_referer={root_referer}&screen_height={screen_height}&screen_width={screen_width}&sourceType=54&staleTime=600000&tz_name=Europe%2FIstanbul&uniqueId={uniqueId}&user_is_login={user_is_login}&webcast_language={webcast_language}&msToken={msToken}",
                "queryString": f"https://www.tiktok.com/api-live/user/room?aid=1988&app_language=en&app_name={app_name}&browser_language={browser_language}&browser_name={browser_name}&browser_online=true&browser_platform={browser_platform}&browser_version={browser_version}&channel=tiktok_web&cookie_enabled={cookie_enabled}&data_collection_enabled={data_collection_enabled}&device_id={device_id}&device_platform={device_platform}&focus_state={focus_state}&from_page=&history_len=6&is_fullscreen={is_fullscreen}&is_page_visible=true&os={os}&priority_region={priority_region}&referer={referer}&region={region}&root_referer={root_referer}&screen_height={screen_height}&screen_width={screen_width}&sourceType=54&staleTime=600000&tz_name=Europe%2FIstanbul&uniqueId={uniqueId}&user_is_login={user_is_login}&webcast_language={webcast_language}&msToken={msToken}",
                "body": "",
                "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
      }

      headers_xGnarly = {
               "Content-Type": "application/json"
      }

      response = requests.post(url_xGnarly, json=data_xGnarly, headers=headers_xGnarly)

      vercel = response.json()
      XGnarly = vercel['xGnarly']
      xbogus = vercel['xbogus']
      signed_url = vercel['signed_url']
      queryString = vercel['queryString']
      query = vercel['query']
      if show_prints == 1:
               print("XGnarly = '{}'".format(XGnarly))
               print("xbogus = '{}'".format(xbogus))
               print("signed_url = '{}'".format(signed_url))
               print("query = '{}'".format(query))
               print("queryString = '{}'".format(queryString))
            
      api_url = f"https://www.tiktok.com/api-live/user/room?aid=1988&app_language=en&app_name={app_name}&browser_language={browser_language}&browser_name={browser_name}&browser_online=true&browser_platform={browser_platform}&browser_version={browser_version}&channel=tiktok_web&cookie_enabled={cookie_enabled}&data_collection_enabled={data_collection_enabled}&device_id={device_id}&device_platform={device_platform}&focus_state={focus_state}&from_page=&history_len=6&is_fullscreen={is_fullscreen}&is_page_visible=true&os={os}&priority_region={priority_region}&referer={referer}&region={region}&root_referer={root_referer}&screen_height={screen_height}&screen_width={screen_width}&sourceType=54&staleTime=600000&tz_name=Europe%2FIstanbul&uniqueId={uniqueId}&user_is_login={user_is_login}&webcast_language={webcast_language}&msToken={msToken}&X-Bogus={xbogus}&X-Gnarly={XGnarly}"
      api_url = signed_url
      if show_prints == 1:
               print(f"api_url: {api_url}")
               print(f"signed_url: {signed_url}")
            
      response = requests.get(api_url, headers=headers)

      # You can now access the response content
      content = response.text

      # Process the content as needed
      #print(content)


      try:
         # 4. Load JSON
         data = json.loads(response.text)
      except Exception as e:
         return {
            "status": "err load json",
            "code": 0,
            "user": user,
            "error": str(e)
         }
      
      room_id = data["data"]["user"]["roomId"]
      user_id = data["data"]["user"]["id"]
      uniqueId = data["data"]["user"]["uniqueId"]
      nickname = data["data"]["user"]["nickname"]
      avatar = data["data"]["user"]["avatarThumb"]
      
      print(f"ROOM_ID:  {room_id}")
      print(f"user_id:  {user_id}")
            
      try:
             startTime = data["data"]["liveRoom"]["startTime"]
      except Exception:
             startTime = None
             pass
      try:
            # 5. Extract the inner stream_data (it's a JSON string inside JSON)
            stream_json_str = data["data"]["liveRoom"]["streamData"]["pull_data"]["stream_data"]

            # convert the inner JSON string → dict
            stream_data = json.loads(stream_json_str)
            print(f"stream_data: {stream_data}")
      
            #live_url_audio = stream_data["data"]["ao"]["main"]["flv"]
            live_url_audio = stream_data.get("data", {}).get("ao", {}).get("main", {}).get("flv")
            #live_url_org = stream_data["data"]["origin"]["main"]["flv"]
            live_url_org = stream_data.get("data", {}).get("origin", {}).get("main", {}).get("flv")
            #live_url_sd = stream_data["data"]["sd"]["main"]["flv"]   
            live_url_sd = stream_data.get("data", {}).get("sd", {}).get("main", {}).get("flv")
            #live_url_hd = stream_data["data"]["hd"]["main"]["flv"]   
            live_url_hd = stream_data.get("data", {}).get("hd", {}).get("main", {}).get("flv")
            #live_url_low = stream_data["data"]["ld"]["main"]["flv"]
            live_url_low = stream_data.get("data", {}).get("ld", {}).get("main", {}).get("flv")            
            if show_prints == 1:
               print("live_url_audio = '{}'".format(live_url_audio))  
               print("live_url_org = '{}'".format(live_url_org))
               print("live_url_sd = '{}'".format(live_url_sd))
               print("live_url_hd = '{}'".format(live_url_hd))
               print("live_url_low = '{}'".format(live_url_low))
            
      except Exception:   
           live_url_audio = None
           live_url_org = None
           live_url_sd = None
           live_url_hd = None
           live_url_low = None
           
      return {
            "status": "ok",
            "code": 1,
            "user": user,
            "uniqueId": uniqueId,
            "nickname": nickname,
            "avatar": avatar,            
            "room_id": room_id,
            "user_id": user_id,
            "startTime": startTime,
            "audio": live_url_audio,
            "org": live_url_org,
            "sd": live_url_sd,
            "hd": live_url_hd,
            "low": live_url_low,            
      }

class more_data(BaseModel):
    followers: list
    blog_url: str
    
@app.post("/more")
async def followers(data: more_data):
    followers = data.followers
    blog_url = data.blog_url
    link_list1 = []
    for url in followers:
        # Send a GET request to the URL and retrieve the web source
        response = requests.get(url)
        web_source = response.text

        link_list = []

        soup = BeautifulSoup(web_source, 'html.parser')
        li_elements = soup.find_all('li')

        for li in li_elements:
            link = li.find('a')['href']
            if blog_url not in link:
               link_list.append(link)

        print(link_list)

        # Extract the profile picture
        profile_picture = soup.find('img', class_='display-thumbnail')['src']
        print("Profile Picture:", profile_picture)

        # Extract the user name
        user_name = soup.find('h1').text.strip().split(' - ')[-1]
        print("User Name:", user_name)

        # base url
        url_parts = url.split("&blogID=")
        base_url = url_parts[0]
        #print(f"base_url: {base_url}")

        # deect user_name language
        text_is_arabic = 0
        print(user_name[1])
        try:
            zz=unicodedata.name(user_name[1])
            print(zz)
            if "LATIN" in zz or "MATHEMATICAL" in zz:            
                print("LATIN")
                #item = unidecode.unidecode(user_name[1])
                #print("{}: is LATIN -{}".format(user_name[1], item))
                text_is_arabic = 0
            if "ARABIC" in zz:            
                print("ARABIC")
                #item = araby.strip_diacritics(user_name[1])
                #print("{}: is ARABIC -{}".format(user_name[1], item))
                text_is_arabic = 1
        except Exception:
            pass

        # text to add to name, so names not repeated!!
        i = 0
        text_list = ['eng ', 'Mr ', 'Dr ', 'ENG ', 'مهندس ']

        if text_is_arabic == 1:
            text_list = ['المهندس ', 'باشمهندس ', 'مهندس ', 'الاستاذ ']
        if text_is_arabic == 0:
            text_list = ['eng ', 'Mr ', 'Dr ', 'ENG ']
    
             
        #url = "https://www.engineerhassan3.com/"  # Replace with the actual URL
        for url in link_list:
            # Send a GET request to the URL and retrieve the web source
            response = requests.get(url)
            web_source = response.text

            # Extract the blog ID from the web source using regular expressions
            blog_id_match = re.search(r"feeds/(\d+)/posts/", web_source)
            if blog_id_match:
                blog_id = blog_id_match.group(1)
                #print("Blog ID:", blog_id)
            else:
                print("Blog ID not found in the web source.")
    
            #
            follower_new_link = f"{base_url}&blogID={blog_id}"
            #print(f"follower_new_link: {follower_new_link}")
            #link_list1.append(follower_new_link)
            link_list1.append({
                        "name": text_list[i] + user_name,
                        "picture": profile_picture,
                        "profileLink": follower_new_link
            })
            if i < len(text_list):
                i+=1
            else:
                i = 0
    
        #print(f"link_list1: {link_list1}")
        #print(link_list1)
    return link_list1
