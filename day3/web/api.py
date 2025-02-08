import requests,json
url="http://api.openweathermap.org/data/2.5/weather?q=hyderabad&units=imperial&appid=ca3f6d6ca3973a518834983d0b318f73"
response=requests.get(url)
print(response.status_code)
print(response.headers)
#print(response.json)
data=json.loads(response.text)
print(type(data))
print(data)
#print(data['weather'][0]['discription'])