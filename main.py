import requests
import json

class main:
    def __init__(self, nickname):
        self.url1 = f'https://api.faceit.com/users/v1/nicknames/{nickname}'

    # get user's id by the nickname
    def get_id(self):
        headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
        r = requests.get(url=self.url1, headers=headers)
        return json.loads(r.text)['payload']['id']

    def friend_request(self):
        url2 = 'https://api.faceit.com/friend-requests/v1/users/a5c3c54a-3de0-4ab7-8653-ac27b0cafa87/requests'
        data = {
            "users": [
                f"{self.get_id()}"
            ],
            "conversionPoint": "profile"
        }

        headers = {
            'authorization':'Bearer 5e4faa22-a44e-4d3e-a088-57be82b9e011',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }

        r = requests.post(url2, headers=headers, data=json.dumps(data))

        return r


if __name__ == '__main__':
    main('nickname').friend_request()



