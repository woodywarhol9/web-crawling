# Python을 활용한 웹 크롤링
[이것이 진짜 크롤링이다 - 기본편](https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%AC%EB%A1%A4%EB%A7%81-%EA%B8%B0%EC%B4%88/dashboard) 강의를 들으며 공부한 내용을 정리합니다.
### 목차

1. [크롤링 기본](#크롤링-기본)
2. [크롤링 팁](#크롤링-팁)
---
## 크롤링 기본
### HTML이란?

- 웹 페이지의 구조를 나타내기 위한 언어
- **태그**로 구성돼 있음

******태그******

- 태그는 시작 태그와 종료 태그로 구성
- `<h1>내용</h1>` 과 같은 형식
- 태그엔 추가적으로 속성명과 속성값이 있을 수 있음
    - `<h1 id=”title”>내용<h1>`과 같은 형식
- 자주 사용되는 태그와 그 역할

| 태그명 | 역할 |
| --- | --- |
| div | 구역 나누기 |
| a | 링크 |
| h1(h2, h3…) | 제목 |
| p | 문단 |
| ul, li | 목록 |

- 태그는 부모 태그와 자식 태그로 구성할 수 있음

```html
<div class="new_info">
	<a href="주소1.com"></a>
	<a href="주소2.com"></a>
	<a href="주소3.com"></a>
</div>
```

- 위 코드에선 `<div>` 태그가 `<a>` 태그의 부모 태그!

### CSS란?

- 웹사이트의 디자인을 표시하기 위한 언어
- 글자 색 변경, 폰트 크기, 가로 세로 길이 변경 가능

**************************CSS 선택자**************************

- 태그 선택자
    - 태그의 이름을 적어서 선택

```html
<h1>제목태그</h1> -> h1으로 선택 가능
<a>링크태그</a> -> a로 선택 가능
```

- id 선택자
    - id 값을 적어서 선택
    - `#articleBody` 같은 형태로 활용

```html
<div id="articleBody>본문내용</div> -> #articleBody로 선택 가능
```

- class 선택자
    - class 값을 적어서 선택
    - `.info_group` 같은 형태로 활용

```html
<div class="info_group">뉴스목록</div> -> .info_group로 선택 가능
```

- 자식 선택자
    - 원하는 태그의 id나 class(별명)이 없을 경우 활용
    - 바로 아래에 있는 태그 선택 가능
    - .`log_sports > span` 같은 형태로 활용

```html
<div class="logo_sports">
	<span>스포츠</span>        -> .log_sports > span으로 선택 가능
</div>
```
## 크롤링 팁
### 검색어 변경하면서 크롤링

![Untitled](https://user-images.githubusercontent.com/86637320/221221554-59966e03-c780-4dec-9e79-2c4c7a7a3834.png)

- parameter 영역을 수정
    - key - value를 변경
    - `where=news`, `query=삼성전자`
- 크롤링하려는 데이터가 여러 곳에 있는지 확인
    - `Ctrl + F` 후 `선택자` 입력

### 주가 크롤링

![Untitled1](https://user-images.githubusercontent.com/86637320/221221655-d55f573e-c509-40d4-ac30-234011ac7571.png)

- 원하는 정보의 태그가 크롤링하기 적합하지 않은 경우, 다른 영역도 확인해보자.
