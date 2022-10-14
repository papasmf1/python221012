# web2.py
#웹서버에 페이지 실행 요청 
import urllib.request
#크롤링 
from bs4 import BeautifulSoup

#페이징을 처리
for i in range(1,6):
url = _ 
    "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page="
data = urllib.request.urlopen(
    "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
soup = BeautifulSoup(data, "html.parser")
#검색하기
cartoons = soup.find_all("td", class_="title")
#<td class="title">
#    <a href="/webtoon/detail">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print( title )
print( link )

for item in cartoons:
    title = item.find("a").text 
    print( title.strip() ) 