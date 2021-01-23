import requests
import datetime
#app id and key for www.nutritionix.com
APP_ID =  "YOUR_APP_ID_GOES_HERE"
API_KEY = "YOUR_API_KEY_GOES_HERE"

#get current date and time
x = datetime.datetime.now()
date = x.strftime("%x")
time = x.strftime("%X")

#endpoint to POST nutritionix
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me which excercises you did? : ")

#docs https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03

#body
params = {
 "query":query,
 "gender":"male",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}

#header
headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "Content-Type": "application/json"
}

response = requests.post(url=endpoint,json = params,headers=headers)
results = response.json()

#endpoint to post sheety
endpoint_sheety = "YOUR_SHEETY_ENDPOINT"

#body of post request for each type of excercise done
for data in results['exercises']:
    body = {
        "workout":{
            "date" : date,
            "time" : time,
            "exercise":data['name'].title(),
            "duration":data['duration_min'],
            "calories":data['nf_calories']
        }
    }
    
    #add each excercise log to googlesheet
    response = requests.post(url=endpoint_sheety,json = body)
    #print status code of your request
    print(response.status_code)
