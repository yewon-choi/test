import requests

token = '1067694791:AAGdlsdUzGJsgnnJv_66DGdSfgb4unKIsvo'
api_url = f'https://api.telegram.org/bot{token}'
anywhere_url = 'choiyewon0623.pythonanywhere.com'

set_webhook_url = f'{api_url}/setWebhook?url={anywhere_url}/telegram'
result = requests.get(set_webhook_url)
print(result.text)

