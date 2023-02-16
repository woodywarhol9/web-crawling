import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text
# html parser 적용
soup = BeautifulSoup(html, "html.parser")
# news_tit 클래스들을 선택
# 결과는 list로 반환
links = soup.select(".news_tit")
for link in links:
    # 기사 제목
    title = link.text # 태그 안에 있는 텍스트 요소 가져오기
    # 기사 링크
    url = link.attrs["href"] # href의 속성 값을 가져온다.
    print(title, url)