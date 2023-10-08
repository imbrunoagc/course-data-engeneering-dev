import requests


class CurrencyConverterAPI:
    def __init__(self, token) -> None:
        self.url = "https://api.freecurrencyapi.com"
        self.token = token
    
    def build_header(self):
        pass

    def build_body(self):
        pass

    def make_request(self, endpoint, method):
        url_request = self.url+endpoint + f"?apikey={self.token}"
        response = requests.request(method=method,
                                    url=url_request)
        return response