import requests
endpoint = 'https://pixe.la/v1/users'

#docs https://docs.pixe.la/entry/post-user
params = {
    "token" :  "YOUR_TOKEN_GOES_HERE",
    "username": "YOUR_USERNAME_GOES_HERE",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

response  = requests.post(url = endpoint,json=params)
print(response.text)
