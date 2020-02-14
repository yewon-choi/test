import requests, pprint, random
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

#텔레그램 API 기본 설정
token = '1067694791:AAGdlsdUzGJsgnnJv_66DGdSfgb4unKIsvo'
api_url =f'https://api.telegram.org/bot{token}'

#네이버
naver_client_id = 'YCJ8nq2q_5ucmUv9Pjr5'
naver_client_secret = 'TOKZdvjWwe'

@app.route('/')
def hello():
    return 'Hello Friend!'

@app.route('/telegram', methods=['POST'])#POST요청으로 보낼 때만 받고, requests.get으로 할 때는 안받겠다!)
def telegram(): #telegram에서 메시지를 보내면
    telegram_response = request.get_json()
    #pprint.pprint(telegram_response)

    if telegram_response.get('message') is not None:
        chat_id = telegram_response.get('message').get('from').get('id')
        text = telegram_response.get('message').get('text')

#기능1. 번역
        if text[0:4] =='/번역 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret}
            data={
                'source' : 'ko',
                'target' : 'en',
                'text' : text[4:]
            }
            papago_response = requests.post(
                'https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data
            )
            text= papago_response.json().get('message').get('result').get('translatedText')

#기능2. 로또_랜덤 숫자 
        if text =='/로또':
            # lotto = random.sample(range(1,46), 6)
            # text = (str(lotto))
            order = sorted(random.sample(range(1,46),6))
            text = str(order)

#기능3. 미세먼지
        if text =='/미세먼지':
           
            url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'

            api_key='mKJD%2Bkyf0Pjt%2Fn4juXswn%2BcTJHfYtVFtlTWa80he0KaK2SSidIOs4TO1JoxQwfjA8kOe7MaInC2P0Os1foVtOg%3D%3D'

            #요청 주소 만들기
            result = f'{url}?ServiceKey={api_key}&sidoName=서울&numOfRows=40&pageNo=1&startPage=3&ver=1.6'
            
            #공공데이터 포털 측에게 요청을 보내고 결과값 가져오기
            response = requests.get(result).text
            #print(response)

            #python 언어가 잘 알아들을 수 있도록 데이터를 구조화하기
            data = BeautifulSoup(response, 'html.parser')

            #구조화된 데이터에서 미세먼지 정보 뽑아내기
            location = data('item')[27]

            #미세먼지 수치 가져오기
            dust = int(location.pm10value.text)
            #station이름 가져오기
            station = location.stationname.text

            if dust > 150:
                dust_rate = '매우나쁨'
            elif 80<dust<=150:
                dust_rate = '나쁨'
            elif 30<dust<=80:
                dust_rate = '보통'
            else:
                dust_rate = '좋음'


            text= f'{station}의 미세먼지 농도는 {dust},{dust_rate}입니다.'


        






        requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')

    return'',200 #200은 잘 받았다는 의미

#우리는 지금 로컬이라서, 임시 주소를 발급받아야한다> ngrok



@app.route('/write')
def write():
    return render_template('write.html')


@app.route('/send')
def send():
    #1. 사용자가 입력한 인풋값 가져오기
    text = request.args.get('message')
    #2. 메시지 내역 가져오기(->getUpdates)
    response = requests.get(f'{api_url}/getUpdates').json()
    #3. 사용자의 chat_id 추출하기
    chat_id = response.get('result')[0].get('message').get('chat').get('id')
    #4. 메시지 전송하기 (->sendMessage)
    message_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(message_url)
    return render_template('send.html')



if __name__ == '__main__':
    app.run(debug=True)