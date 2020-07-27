import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = '838890559:AAHO1myIz4tdHgG33wMZwVBgEBHXdkZk8WA')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200727'

def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if(imax):
        imax = imax.find_parent('div',class_='col-times') #class가 col-times인 것에 하위 부분에 제목 존재
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id= 1303263161, text = title + '의 IMAX 예매가 열렸습니다.')
        