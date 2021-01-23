import requests

#docs https://docs.pixe.la/entry/post-graph

USERNAME = "YOUR_USERNAME_GOES_HERE"
TOKEN = "YOUR_TOKEN_ID_GOES_HERE"

endpoint = "https://pixe.la/v1/users/{}/graphs".format(USERNAME)

params = {"id":"bio-graph","name":"bio-walk","unit":"km","type":"float","color":"shibafu"}

headers = {
    "X-USER-TOKEN" : TOKEN
}

response = requests.post(url=endpoint,json=params,headers=headers)
print(response.text)