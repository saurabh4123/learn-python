#a way to create our own api that fetchs us data from websites that dont have public api
import requests

url="https://pixelford.com/blog/"
response = requests.get(url)
print(response.content) #.content prints the whole html code
#due to so many requests securuty software is blocking out requests
print(requests.utils.default_headers())
#as we can see it uses python agent we need to change it since server sees it and block our request
#changing user-agent is one of the workaround
response = requests.get(url ,headers= {'user-agent': 'Hello'}) #this fixes things or you can use random number in place of hello or copy your user agent from browser and paste it
print(response.content)


