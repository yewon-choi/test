import random, requests
from bs4 import BeautifulSoup
from datetime import datetime
from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello, Flask!'
    return render_template('main.html')

@app.route('/ssafy')
def ssafy():
    return '싸피짱!ㅎㅎ'

@app.route('/dday')
def dday():
    today = datetime.now() #오늘 날짜
    endgame = datetime(2021,1,5)
    result = endgame - today
    return f'수료까지 {result.days}일 남았습니다.'

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
@app.route('/board/<int:number>')
def board(number):
    # return f'{number}번 게시글입니다.'
    content = '안녕하세요, 잘 보여요?ㅎㅎㅎㅎ'
    return render_template('board.html', board_number=number, content=content)

#실습
#1. greeting html 파일 생성 - greeting.html
#2. 함수에서 greeting html 파일 렌더링
#-render_template
#-변수 값 넘겨주기

@app.route('/greeting/<string:name>')
def greeting(name):
    # return f'환영합니다, {name}님!'
    excercises = ['벤치프레스','랫풀다운','맨손팔굽']
    return render_template('greeting.html', name=name, excercises=excercises)






#실습
#사용자로부터 숫자값을 받아서 세제곱을 return하는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3}입니다.'

#실습
# url을 통해 사람 수 입력하기
import random
@app.route('/lunch/<int:number>')
def lunch(number):
     #1. 중국집 메뉴 리스트 만들기
     chinese_foods = ['짜장면', '짬뽕','탕수육','볶음밥','유산슬']
     
     #if people > len(chinese_foods):
     #return f'{len(chinese_foods)} 명보다 적게 입력해라^^'
     #2. 사용자가 입력한 사람 수만큼 메뉴 랜덤으로 뽑기
     order = random.sample(chinese_foods,number)
     #order = random.sample(chinese_foods, number)
     #3. 리스트를 문자열로 변환하기
     result = ', '.join(order)
     
     #4. 결과값  return 해주기
     return str(result)

#사용자가 텍스트를 입력할 수 있는 박스를 건네주는 로직
@app.route('/ping')
def ping():
    return render_template('ping.html')


#사용자가 입력한 텍스트를 받아서 가공한 뒤 사용자에게 돌려주는 로직
@app.route('/pong')
def pong():
    user_id = request.args.get('user_id')
    user_secret = request.args.get('user_secret')
    return render_template('pong.html', user_id=user_id, user_secret=user_secret)
    
    # return '회원가입 완료!'

#

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

# @app.route('/godmademe')
# def godmademe():
    # return render_template('godmademe.html')

@app.route('/godmademe')
def godmademe():
   
   #사용자가 인풋 태그에 입력한 값 가져오기
    name = request.args.get('name')

    #특성들이 담긴 리스트 만들기
    first_list = ['엉뚱함','자신감','쑥스러움','애교','잘난척']
    second_list = ['식욕','돈복','물욕','허세']
    third_list = ['잘생김','못생김','있어도그럼','그저그럼']

    #random
    a1 = random.choice(first_list)
    a2 = random.choice(second_list)
    a3 = random.choice(third_list)
    return render_template('godmademe.html', name=name, a1=a1, a2=a2, a3=a3)


@app.route('/dust')
def dust():
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    api_key='mKJD%2Bkyf0Pjt%2Fn4juXswn%2BcTJHfYtVFtlTWa80he0KaK2SSidIOs4TO1JoxQwfjA8kOe7MaInC2P0Os1foVtOg%3D%3D'
    result = f'{url}?ServiceKey={api_key}&sidoName=서울&numOfRows=40&pageNo=1&startPage=3&ver=1.6'
    response = requests.get(result).text
    data = BeautifulSoup(response, 'html.parser')
    location = data('item')[27]
    dust = int(location.pm10value.text)
    station = location.stationname.text

    if dust > 150:
        dust_rate = '매우나쁨'
    elif 80<dust<=150:
        dust_rate = '나쁨'
    elif 30<dust<=80:
        dust_rate = '보통'
    else:
        dust_rate = '좋음'

    return render_template('dust.html', station=station, dust=dust, dust_rate=dust_rate)

#반드시 app.py 최하단에 위치
if __name__ =='__main__':
    app.run(debug=True)



     