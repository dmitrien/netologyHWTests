import json
import requests



with open('../tokenYD.txt', 'r') as file_object:
    tokenYD = file_object.read().strip()

host = 'https://cloud-api.yandex.net/v1/disk/resources?path='
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'OAuth {}'.format(tokenYD)
}

def create_folder(path):
    requests.put(host + path, headers=headers)

def show_folder(path):
    return requests.get(host + path, headers=headers).status_code

def delete_folder(path):
    requests.delete(host + path, headers=headers)





