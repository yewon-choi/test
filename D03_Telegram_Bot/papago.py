#NAVER API KEY 정보
naver_client_id = 'YCJ8nq2q_5ucmUv9Pjr5'
naver_client_secret = 'TOKZdvjWwe'

#요청 url
naver_url = 'https://openapi.naver.com/v1/papago/n2mt'

# 요청할 때 함께 보낼 부가정보
data = {
    'source' : 'ko',
    'target' : 'en',
    'text' : '잘 지내세요?'
}

#요청할 때 함께 보낼 사용자 정보
headers = {
    'X-Naver-Client-Id': naver_client_id,
    'X-Naver-Client-Secret' : naver_client_secret
}

import requests, pprint
papago_response = requests.post(naver_url, headers=headers, data=data) #원래는 gets 인데, 네이버는 포스트!다른공간에 담아서 보내준다.

pprint.pprint(papago_response.json())

