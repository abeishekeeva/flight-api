from typing import Counter
import requests

class APIConsumer:
    def __init__(self,url,token):
        self.url = url
        self.token = token

    def make_request(self):
        response = requests.get(self.url, headers={'Authorization' : f'Token {self.token}'})
        if response.status_code == 200:
            counter = 0
            for item in response.json():
                if item['airport_code'][0] == 'A':
                    counter += 1
            #Вернуть кол-во аэропортов 
            return f"Кол-во аэропортов: {len(response.json())}"
        else:
            return {"err_msg": "Request error"}



flight_api = APIConsumer('http: //127.0.0.1:8000/api/airports/','ba1a0a7befe4b95cd86efb60f6a2f32bb0e13b17')
print(flight_api.make_request())

