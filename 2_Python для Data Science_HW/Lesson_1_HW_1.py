import requests
from pprint import pprint
import json

token='3064bc713064bc713064bc716b3002bc8f330643064bc716bf5d61572920cfe6eda3f78'

main_link='https://api.vk.com/method/users.get?user_ids=210700286&fields=bdate&' # не стал заморочиватся с оновной ссылкой!

req=requests.get(f'{main_link}ccess_token={token}&v=5.102')

if req.ok:
    data=json.loads(req.text)
    pprint(data)

