from pprint import pprint

import requests
with open('file.txt', encoding='utf-8') as f:
    token = f.read()

class YaUploader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_headers(self):
        return {
            'Accept': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
        }

    def upload(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources/publish"
        headers = self.get_headers()
        params = {'path': self.file_path, 'overwrite': 'true'}
        r = requests.put(url=url, params=params, headers=headers )
        pprint(r.json())
        if r.status_code == 201:
            pprint("Success")
        else:
            pprint(f'Ошибка {r.status_code}')


if __name__ == '__main__':
    uploader = YaUploader('C//Zima.jpg')
    result = uploader.upload()
