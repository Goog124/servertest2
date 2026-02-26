import requests
from my_token import TOKEN
import pprint

server = 'https://cloud-api.yandex.net/v1/disk/resources/files'
headers = {
    'Authorization': TOKEN
}

data = requests.get(server, headers=headers)
pprint.pprint(data.json())

