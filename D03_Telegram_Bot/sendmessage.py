import requests, pprint

#기본 정보
token = '1067694791:AAGdlsdUzGJsgnnJv_66DGdSfgb4unKIsvo'
api_url =  f'https://api.telegram.org/bot{token}'
#chat_id = '1031092215'

#봇에게 들어온 메시지 내역 가져오기
update_url = f'{api_url}/getUpdates'
response = requests.get(update_url).json()
#pprint.pprint(response)

#사용자의 chat_id 추출하기
chat_id = response.get('result')[0].get('message').get('chat').get('id')

#print(chat_id)

#답장 보내기
text = '둘셋둘셋 테스트'
message_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url)







# #답장 보내기
# text = '헛둘헛둘 테스트'
# message_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'

# #요청 보내기
# requests.get(message_url)
