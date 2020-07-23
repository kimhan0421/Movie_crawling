import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200724'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
imax = soup.select_one('span.imax')

if(imax):
    imax = imax.find_parent('div',class_='col-times') #class가 col-times인 것에 하위 부분에 제목 존재
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    print(title + '의 IMAX 예매가 열렸습니다.')
else:
    print('IMAX를 찾을 수 없습니다.')