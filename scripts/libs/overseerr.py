import requests


class Overseerr:
    def __init__(self, base_url, api_key):
        if not base_url or not api_key:
            raise Exception('Missing Overseerr URL or API key')

        self.url = base_url.rstrip('/') + '/api/v1'
        self.api_key = api_key
        self.headers = {
            'X-Api-Key': api_key
        }

        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def get_status(self):
        response = self.session.get(f'{self.url}/status')
        response.raise_for_status()
        status = response.json()

        return status

    def get_requests(self):
        response = self.session.get(f'{self.url}/request')
        response.raise_for_status()
        requests = response.json()

        return requests
