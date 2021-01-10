import requests
import pandas as pd
import sys
from slacker import Slacker
from slack_print import SlackPrint


client_id = "SroSIISIdjj0ywcLmi6"  #Naver.com api id 
client_secret = "MeIrW_iiDS"     #Naver.com api passcode


sp = SlackPrint('xoxb-1594365443077-158147729702-WUDIDJDJ', 'stock')


search_word = '뉴욕증시' #Search
encode_type = 'json' #
max_display = 55 #Number of News
sort = 'date' #arrange order
start = 1 # print location

url = f"https://openapi.naver.com/v1/search/news.{encode_type}?query={search_word}&display={str(int(max_display))}&start={str(int(start))}&sort={sort}"

#id & passcode on header
headers = {'X-Naver-Client-Id' : client_id,
           'X-Naver-Client-Secret':client_secret
           }

#HTTP
r = requests.get(url, headers=headers)
#HTTP result if 200 = success
print(r)

# sp.print(r.json()) # if you want to print url for News titles as well

sp.print(pd.DataFrame(r.json()['items']))







