from src.api import CurrencyConverterAPI
from src.file_handler import FileHandler
from env import define_env
import os
import json

define_env()

token = os.getenv("TOKEN")
if not token:
    raise Exception("Sem token...")
curr_convert = CurrencyConverterAPI(token=token)
file_handler = FileHandler()
response = curr_convert.make_request(endpoint="/v1/currencies",
                                     method="get")
json_data = json.loads(response.content.decode("utf8"))
file_handler.store_data(json_data)