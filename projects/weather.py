#using the weather api
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#get api key from openweathermap website after logging in
#api basically return a json which is a dictionary with collection of lists

#first we need to install requests module since its not a standard one
import requests as rs

# #we can use try and except in case there is no internet access
# try:
#     #get the data
#     response = rs.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=26.8467&lon=80.9462&appid=30ff0fb3b99a47d67802efc80bead234")
    
# except:
#     print("No internet access!! :(")

# #we can creatre a virtual environment also so that we can switch between environments whenever required
    
# resp_json=response.json()
# print(resp_json)

# city=resp_json["name"]
# temp=resp_json["main"]["temp"]
# temp_min=resp_json["main"]["temp_min"]
# temp_max=resp_json["main"]["temp_max"]
# print(f"Your city is ->{city}")
# print(f"Temp in {city} is {temp}°C.")
# print(f"Today's high: {temp_min}°C")
# print(f"Today's low: {temp_max}°C")

class City:
    def __init__(self,lat,lon,units="metric"):
        self.lat=lat
        self.lon=lon
        self.units=units
        self.get_data()#every time we create object this function is called..

    def get_data(self):
        try:
            response = rs.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=30ff0fb3b99a47d67802efc80bead234")
        except:
            print("No internet access!! :(")            
        resp_json=response.json()
        self.city=resp_json["name"]
        self.temp=resp_json["main"]["temp"]
        self.temp_min=resp_json["main"]["temp_min"]
        self.temp_max=resp_json["main"]["temp_max"]

    def temp_print(self):
        print(f"Your city is ->{self.city}")
        print(f"Temp in {self.city} is {self.temp}°C.")
        print(f"Today's high: {self.temp_min}°C")
        print(f"Today's low: {self.temp_max}°C")
        

#city1
myCity1=City(26.8467,80.9462)
myCity1.temp_print()

#city2
myCity2=City(35.652832,139.839478)
myCity2.temp_print()




