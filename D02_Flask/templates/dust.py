import requests
from bs4 import BeautifulSoup

#필요한 정보
url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'

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

print(station,dust)

if dust > 150:
    dust_rate = '매우나쁨'
elif 80<dust<=150:
    dust_rate = '나쁨'
elif 30<dust<=80:
    dust_rate = '보통'
else:
    dust_rate = '좋음'

print(f'{station}의 미세먼지 농도는 {dust},{dust_rate}입니다.')