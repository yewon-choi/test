# Flask 서버 기초

## 1. Flask Intro

* Flask 공식문서



### 1.1 Flask 설치 및 서버 실행

* 설치하기

  ```cmd
  $ pip install Flask
  ```

* 설치확인

  ```cmd
  Package           Version
  ----------------- ----------
  
  colorama          0.4.3
  *Flask             1.1.1*
  idna              2.8
  isort             4.3.21
  itsdangerous      1.1.0
  Jinja2            2.10.3
  lazy-object-proxy 1.4.3
  MarkupSafe        1.1.1
  mccabe            0.6.1
  pip               19.3.1
  pylint            2.4.4
  requests          2.22.0
  setuptools        40.8.0
  six               1.13.0
  soupsieve         1.9.5
  typed-ast         1.4.1
  urllib3           1.25.7
  Werkzeug          0.16.0
  wrapt             1.11.2
  ```

* 기본 코드 작성

  ```python
  #app.py
  
  from flask import Flask
  
  app = Flask(__name__)
  
  @app.route('/')
  def hello_world():
      return 'Hello, Flask!'
  ```

  

* 개발용 서버 실행

  프롬프트 경로가 app.py가 있는 경로에 위치했는지 반드시 확인 후 명령어 실행!

  ```cmd
  $flask run
  ```

  ![image-20200116131204050](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200116131204050.png)

  

### 1.2 여러 페이지 만들어보기

* 경로를 다르게 하여 페이지 생성

  ```python
  from datetime import datetime
  from flask import Flask
  
  app = Flask(__name__)
  
  @app.route('/')
  def hello_world():
      return 'Hello, Flask!'
  
  @app.route('/ssafy')
  def ssafy():
      return '싸피짱!ㅎㅎ'
  
  @app.route('/dday')
  def dday():
      today = datetime.now() #오늘 날짜
      endgame = datetime(2021,1,5)
      result = endgame - today
      return f'수료까지 {result.days}일 남았습니다.'
  ```

* 문자열이 아니라  HTML 태그도 인식한다.

  ```python
  @app.route('/html')
  def html():
      return '<h1>제목 큼지막하죠?</h1>'
  
  @app.route('/html_line')
  def html_line():
      return """
      <h1>여러줄 잘 나옵니까?</h1>
      <ul>
          <li>1등</li>
          <li>2등</li>
      </ul>
      """
  ```

  

### 1.3 Variable Routing

> 사용자의  URL 요청값을 가져와서 활용할 수 있다.

* Board

  게시글을 보여주는 템플릿(껍데기)을 만들어 두고, 데이터베이스에서 해당 게시글 번호에 맞는게시글 정보를 가져와서 템플릿 안에 넣어주기만 하면 된다.

  ex) 100개의 게시글이 있다고 해서, 100개의 페이지를 만드는 것은 비효율적이다.

  ```python
  @app.route('/board/<int:number>')
  def board(number):
      return f'{number}번 게시글입니다.'
  ```

  

* Greeting

  ```python
  @app.route('/greeting/<string:name>')
  def greeting(name):
      return f'환영합니다, {name}님!'
  ```



* Cube

  ```python
  @app.route('/cube/<int:number>')
  def cube(number):
      return f'{number}의 세제곱은 {number**3}입니다.'
  ```

  

## 1.4 서버 실행 방식 바꾸기

> app.py 코드가 바뀔 때마다 서버를 재시작 하는 것이 매우 번거롭다. 소스 코드가 바뀌면  Flask 가 코드의 변경 사항을 자동으로 파악하고 서버에 반영하도록 만들어보자!

* Flask는 기본적으로   debug 모드가 꺼져있는 상태다.  debug 모두를 켜면 소스코드 변경 사항이 저장과 함게 서버에 바로 반영된다.

* 최하단에 소스 코드 추가

  ```python
  from flask import flask
  app = Flask(__name__)
  ...
  ...
  ...
  ...
  #반드시 app.py 최하단에 위치
  if __name__=='__main__':
      app.run(debug=True)
  ```

* `python app.py` 명령어를 통해 서버를 실행한다.

  * 이전처럼  flask run 명령어를 사용하면, 소스코드 변경사항이 자동으로 반영되지 않으니 반드시  python app.py 명령어로 서버를 실행하자
  * 명령어 실행 전, app.py가 있는 경로에 위치했는지 반드시 확인하자.

  ```bash
  C:\Users\multicampus\Desktop\startcamp>
  $ python app.py
  ```

  