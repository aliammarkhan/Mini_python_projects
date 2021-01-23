import datetime
import requests

# docs https://docs.pixe.la/entry/post-pixel

USERNAME = "YOUR_USERNAME_GOES_HERE"
TOKEN = "YOUR_TOKEN_ID_GOES_HERE"
GRAPH_ID = "GRAPH_ID_GOES_HERE"

#graph endpoint where we want to store our data
endpoint = "https://pixe.la/v1/users/{}/graphs/{}".format(USERNAME,GRAPH_ID)

#get the date in specfied format
today = datetime.datetime.now().strftime("%Y%m%d")

#body of post request
params = {"date":today,"quantity":"2.3"}
#header sent with request
headers = {
    "X-USER-TOKEN" : TOKEN
}
#post a requests
response = requests.post(url = endpoint,json = params,headers=headers)
print(response.text)


