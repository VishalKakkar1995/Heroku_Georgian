from flask import Flask, request
import json 
import random
import requests
app = Flask(__name__)
app.debug = True

print("Working")

app= Flask(__name__)
app.debug= True


@app.route('/')
def hello():
    return '{"Hello": "This is Vishal Kakkar - 200535056"}'

@app.route('/webhook',methods=['POST'])
def index():
    #Get the geo-city entity from the dialogflow fullfilment request.
    body = request.json
    city= body['queryResult']['parameters']['geo-city']
    if city=="" or city==" ":
        city= body['queryResult']['parameters']['geo-state']


    #Connect to the API anf get the JSON file.
    api_url='https://api.postalpincode.in/postoffice/'+ city
    headers = {'Content-Type': 'application/json'} #Set the HTTP header for the API request
    response = requests.get(api_url, headers=headers) #Connect to openweather and read the JSON response.
    r=response.json() #Conver the JSON string to a dict for easier parsing.

    #Extract weather data we want from the dict and conver to strings to make it easy to generate the dialogflow reply.
    Postalcode = str(r["PostOffice"]["Pincode"])

    #build the Dialogflow reply.
    reply = '{"fulfillmentMessages": [ {"text": {"text": ["The postal code of '+ city + ' is ' + Postalcode + '"] } } ]}'
    return reply