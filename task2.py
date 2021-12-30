
import  requests

TOKEN = ''

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Accept': 'application/json',
                   'Authorization': 'OAuth ' + self.token}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params).json()
        return response['href']

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        file_to_send = '/' + file_path.rsplit('/', 1)[-1]
        file_dir = '/test'
        href =  self._get_upload_link(file_dir+file_to_send)
        with open(file_path, 'rb') as file:
            response = requests.put(href, data=file)
        return response

if __name__ == '__main__':
    path_to_file = '/'
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

