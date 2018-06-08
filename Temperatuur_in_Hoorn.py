"""
Kijken of ik de internet temperatuur kan ophalen
"""
# voorbeeld gevonden op internet
# https://gathering.tweakers.net/forum/list_messages/1654993

import urllib.request
import json
import datetime
import time
    
# set parameters
date = (datetime.datetime.now().strftime("%d-%m-20%y"))
time = (datetime.datetime.now().strftime("%H:%M"))
day_of_the_week = (datetime.date.today().strftime("%A"))

# key ophalen bij https://home.openweathermap.org/api_keys
key = "233701779ae96b795e27bee825342a90"

# plaatsen nabij Lutjebroek zijn Hoorn en Venhuizen
place = "Hoorn"

# bron is openweathermap.org
url = "http://api.openweathermap.org/data/2.5/weather?q=" + place + "&appid=" + key + "&units=metric"

response = urllib.request.urlopen(url)
data = json.loads(response.read())

# temperatuur variable
temp = data['main']['temp']
humidity = data['main']['humidity']
temp_min = data['main']['temp_min']
temp_max = data['main']['temp_max']

# uitlezen waarde, ik krijg het nog niet netjes naast elkaar
print ("Op " + date + " om " + time + " uur, was het in " + (place) + " " + str(temp) + " graden.")
print ("De luchtvochtigheid was " + str(humidity) + "%.")
print ("De minimum temperatuur vandaag is " + str(temp_min) + " graden.")
print ("De maximum temperatuur vandaag is " + str(temp_max) + " graden.")
