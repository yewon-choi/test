# HTML Basic

## 1.HTML이란?

> Hyper Text Markup Language의 약어

* 웹 페이지를 만들기 위한 언어로, 웹 브라우저 위에서 작동하는 언어다.
* 웹 페이지를 기술하기 위한 마크업 언어다.
  * 이 단어는 강조가 필요하니까 표시(마킹)를 해야지!



## 2.문서의 기본 구조

* 확장자는 html 혹은 htm으로 끝난다.
* `<!DOCTYPE html>` : 문서의 형식이 html이라고 선언한다.
* `<html>`: 최상위 태그, 하위에 `<head>` 태크와  `<body>`태그를 가지고 있다.
  * `<head>`: 문서를 설명하는 태그
  * `<body>`: 사용자가 실제 눈으로 보게되는 문서 내용이 위치한다.



```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>HTML Basic</title>>
    </head>
    
    <body>
         
    </body>
</html>
```



## 3.여러 가지 HTML 태그

* `<h1>`~`<h6>` : 제목을 나타내는 태그
* `<p>` : 문단을 나타내는 태그
* `<a>` : 링크를 표시하는 앵커 태그
  * href에 이동할 웹 페이지의 주소를 입력한다.
* `<ul>` : 순서가 없는 비순차 리스트 태그
* `<ol>` : 순서가 있는 순차 리스트 태크
* `<li>` : 리스트 아이템 태그
* `<form>` : 사용자가 입력한 값이 어느 곳으로 전달될 지 결정하는 폼 태그
* `<input>`: 사용자로부터 입력을 받을 때 사용하는 인풋 태그

```python
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>HTML Basic</title>>
    </head>
    
    <body>
        <!--제목 및 본문-->
        <h1>h1 태그입니다.</h1>
        <h2>h2 태그입니다.</h2> 
        <h6>h6 태그입니다.</h6> 
   
        <!--링크 태그-->
        <a href="https://www.naver.com/">네이버 바로가기</a>
        
        <!--리스트 태그-->>
        <ul>
            <li>순서가 없는 리스트</li>
            <li>순서가 없는 리스트</li>
        <ul>
        <ol>    
            <li>순서가 있는 리스트</li>
            <li>순서가 있는 리스트</li>
        </ol>

        <!--사용자 입력을 받기 위한 태그-->>
        <form action="https://search.naver.com/search.naver">
            <input type="text" name="query" placeholder="검색어를 입력해주세요.">
            <input type="submit" value="검색하기">
        </form>
        <form action="https://www.google.co.kr/search">
            <input type="text" name="q" value="SSAFY">
            <input type="submit" value="구글검색">
        </form>
    </body>
</html>
```

