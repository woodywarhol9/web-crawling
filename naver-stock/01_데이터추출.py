import requests
from bs4 import BeautifulSoup

# 종목 코드 리스트
codes = ["005930", "000660", "035720"]

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    # url에서 데이터 가져옴
    response = requests.get(url)
    # html 영역
    html = response.text
    # parsing이 어려우니 활용
    soup = BeautifulSoup(html, "html.parser")
    # select_one 실행 시 strong 태그 출력 -> text만 필요
    price = soup.select_one("#_nowVal").text
    # "," 제거
    price = price.replace(",", "")
    print(price)