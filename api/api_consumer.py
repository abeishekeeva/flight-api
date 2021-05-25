import requests 

class APIConsumer:
    
    def __init__(self, url, token):
        self.url = url 
        self.token = token 

    def make_request(self):
        response = requests.get(self.url, headers={'Authorization': f'Token {self.token}'})
        if response.status_code == 200: 
            counter = 0 
            for item in response.json():
                if item['airport_code'][0] == 'B':
                    counter += 1            
            return f"Кол-во аэропортов: {counter}"
        else: 
            return {"err_msg": "Request error"}

    
flight_api = APIConsumer('http://127.0.0.1:8000/api/airports/', 'b00ea1604f7ad04f321ed30bd07cd67b5842c557')
print(flight_api.make_request())

APIConsumer.exchange('AUD', 'USD', 300)