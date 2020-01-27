import requests
import time
import csv
import os.path

r = requests.get('https://api.openweathermap.org/data/2.5/group?id=2172517,4140963,1273293,524901,3369157,108410&appid="your api key"')
json_object = r.json()
weather_data = json_object['list']

file_exists = os.path.isfile("path of your csv")

with open('weather.csv','a') as out_file:
    writer=csv.writer(out_file,lineterminator='\n',)
    if not file_exists:
    	writer.writerow(["Temprature","Humidity","City","Country","Weather_description","Coordinates"])
    while True:
    	time.sleep(2)
    	for i in weather_data: 
	    	temprature,humidity = float(i['main']['temp']),float(i['main']['humidity'])
	    	city_name,country = i['name'],i['sys']['country']
	    	description = i['weather'][0]['description']
	    	lat,lon= str(i['coord']['lat']),str(i['coord']['lon'])
	    	coordinates=lat+","+lon
	    	rows = [temprature,humidity,city_name,country,description,coordinates]
	    	writer.writerow(rows)