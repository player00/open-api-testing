import requests


class RequestsWrapper:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        return requests.get(f"{self.base_url}/{endpoint}")

    def post(self, endpoint, payload):
        return requests.post(f"{self.base_url}/{endpoint}", json=payload)

    def put(self, endpoint, payload):
        return requests.put(f"{self.base_url}/{endpoint}", json=payload)

    def patch(self, endpoint, payload):
        return requests.patch(f"{self.base_url}/{endpoint}", json=payload)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}/{endpoint}")
