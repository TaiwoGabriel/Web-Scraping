import pandas as pandas
from bs4 import BeautifulSoup
import requests
import lxml

#Request Permission

#Define URL
url = 'https://sports.bet9ja.com/popularCoupons/0/englandpremierleague/492'

#Ask hosting server to fetch URL
requests.get(url)

pages = requests.get(url)
print(pages.text)
