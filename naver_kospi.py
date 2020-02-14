import requests
from bs4 import BeautifulSoup

#1. requests  모듈을 이용해서 네이버 금융 웹 페이지 정보 가져오기
response = requests.get('https://finance.naver.com/sise/').text

#2. BeautifulSoup 이용해서 웹 페이지를 가공하기 쉬운 형태로 바꾸기
data=BeautifulSoup(response, 'html.parser')

#3. 가공된 데이터에서 고스피 지수만 가져오기
kospi = data.select_one('#KOSPI_now')
print(kospi.text)
