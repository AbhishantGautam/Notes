#------------------------------------------------  INTRODUCTION  -------------------------------------------------------------------------------------#
'''
-- API : application programming interface : are set commands, functions, protocols and objects that programmers can use to interact
         with external systems.
-- API : interface between you and the external system
-- we make request to external system to provide some data, while staying within the rules of that specific API
-- if we fulfill all the rules of that API, external system will respond with data
-- API endpoint : The url from where we want to extract data from (eg: api.coinbase.com)
-- when we put api endpoint in the url-box of chrome, it gives us the required data
-- API returns data in the form of JSON format 
'''

#making an api call:
# pip install requests
import requests #this module is used to make http requests across internet
response = requests.get(url="website's API endpoint")
data = response.json() #------------> returns a dictionary containing the required data from endpoint.
# datatype of response variable -----------> response code datatype

'''
response code/ HTTP code : tells the status of our api request call.
    1xx = hold on, im processing
    2xx = everything went as planned
    3xx = go away, (but it was not your problem)
    4xx = You screwed up
    5xx = I screwed up
'''
response = requests.get(url="api endpoint")
response.raise_for_status() #-------->tells us what the HTTP code really means

# API parameters: Arguments to API call which guides the API on what type of data we want from endpoint
# not all APIs have parameters

parameters = {
    "lat" : 0.11235,
    "lng" : 0.12354
}
response = requests.get("end point", params = parameters) #passing arguments to api call

'''
API url : https://opentdb.com/api.php    ?    amount=10&type=boolean
                   api endpoint                     parameters        
-- api endpoint and entered parameters are seperated by a "?" sign.
'''

#when we import data from api, some characters look weird. like " is replaced by &quot and ' is replaced by &#039 
# these are called "HTML entities". to avoid them, do:
text = "some weird looking data we got from api"
import html
print(html.unescape(text))

#api authentication : some APIs deal with important info and hence charge some money. 
#the ones who pay money get an API_KEY, and they can get data only if they have this key. this is called api authentication
'''
API url : https://opentdb.com/api.php    ?    amount=10&type=boolean    &    appid={your_api_key}
                   api endpoint                     parameters                     API key  
-- api endpoint and entered parameters are seperated by a "?" sign. parameters and api key seperated by "&" sign.
'''

#https, "s" stands for secure. ie: api info we entered (endpoint, api key, other info) is actually encrypted and cant be hacked

#http headers: optional keyword arguments. Whatever we enter under headers is not visible to anybody
'''
header_1 = {
    "X-USER-TOKEN" : TOKEN
}
'''