import requests
from bs4 import BeautifulSoup
import pyautogui
# 페이지가 변경될 때 마다 start가 변경 됐음 -> start 값을 바꿔주면
# 여러 페이지 결과 모두 확인 가능
keyword = pyautogui.prompt("검색어를 입력하세요.")
# str로 리턴 됨!
lastpage = pyautogui.prompt("크롤링할 페이지 수를 입력하세요.")
# 페이지 번호 표시
pageNum = 1
for i in range(1, int(lastpage) * 10, 10):
    print(f"{pageNum} 페이지 입니다. ======================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
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
    pageNum = pageNum + 1