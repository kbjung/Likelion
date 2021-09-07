import requests
import json

city = "Seoul"
apikey = "87e33f2db1e3cb8ff674e5567988d7b4"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

result = requests.get(api)
print(result.text)

data = json.loads(result.text)

print(type(result.text))
print(type(data))