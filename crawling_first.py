import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0056&date=20200724'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.select('div.info-movie') #리스트 형태로 들어감
for i in title_list:
    print(i.select_one('a > strong').text.strip())