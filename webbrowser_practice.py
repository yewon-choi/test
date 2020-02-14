#1. webbrowser 모듈 불러오기
import webbrowser

#2.검색할 단어 리스트 만들기
artists = ['민수','아이유','레드벨벳','있지','BTS']

#3. 단어 리스트 반복문 돌려서 네이버 검색창 띄우기 : webbrowser.open_new(주소)
for artist in artists:
  webbrowser.open_new('https://search.naver.com/search.naver?query=%s'%artist)


