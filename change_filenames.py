#1. import 모듈 들고오기
import os
#2. 작업 경로 이동하기
os.chdir(r'C:\Users\multicampus\Desktop\dummy')

#3.작업 경로에 있는 파일 목록 가져오기
filenames = os.listdir()
print(filenames)

#4. 파일명 바꾸기
for filename in filenames:
    os.rename(filename, filename.replace('SAMSUNG_','SSAFY_'))
