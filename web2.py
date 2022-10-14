# web2.py
#웹서버에 페이지 실행 요청 
import urllib.request
#크롤링 
from bs4 import BeautifulSoup

for i in range(1,6):
    url = \
    "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page="+str(i)
    print( url )
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")

    for item in cartoons:
        title = item.find("a").text 
        print( title.strip() ) 