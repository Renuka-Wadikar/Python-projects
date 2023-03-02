import requests

API_key = '8fbb1972123440a2c97baec1983b7998'

def get_data(place, forecast_days=None):
    url =f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}'
    response = requests.get(url)
    content = response.json()
    filtered_data = content['list']
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__=='__main__':
    print(get_data(place='Pune',forecast_days=3))