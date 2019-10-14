import requests
import json

#базовый_путь
main_link = 'https://api.github.com/'

#рандомный юзер
user = 'nickoala'


# делаем запррс и добавляем в цикле в список только наименования репозитория
req = requests.get(f'{main_link}users/{user}/repos')
list_repos = []
if req.ok:
    data = json.loads(req.text)
    for x in range(0, len(data)):
        list_repos.append(data[x]['name'])

#сохраняем весь резльтута запроса и выводим список
with open('data.json', 'w') as f:
    json.dump(data, f)

print(list_repos)
