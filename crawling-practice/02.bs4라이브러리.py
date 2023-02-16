import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com")
html = response.text
# html parser 활용
soup = BeautifulSoup(html, "html.parser")
# #은 CSS 선택자
# 원하는 태그 1개만 가져오고 싶을 땐 select_one, 전부 가져오고 싶을 땐 select
word = soup.select_one("#NM_set_home_btn") # '네이버를 시작 페이지로' a 태그의 id
# text만 출력
print(word.text)
# 출력 결과
"""
네이버를 시작페이지로
"""