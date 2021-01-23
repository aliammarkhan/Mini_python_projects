import requests
from bs4 import BeautifulSoup
import lxml
from urllib.request import urlopen
import smtplib

#email and password 
email = 'EMAIL_GOES_HERE'
password = 'PASSWORD_GOES_HERE'


#get the html from the product link

#headers that are sent by the browser with each request
#http://myhttpheader.com/
header = {
    'Request Line' : 'GET / HTTP/1.1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Accept-Language':'en-US,en;q=0.9',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate',
    'X-Http-Proto':'HTTP/1.1',
    'X-Real-Ip':'51.15.192.242',
    }
#link to the headphones i want
product_url = 'https://homeshopping.pk/products/Redragon-ARES-H120-Gaming-Headset-with-Microphone-for-PC-Price-in-Pakistan.html'
#get the html
html = requests.get(product_url,headers=header).text

#create soup object
soup = BeautifulSoup(html,"lxml")

#the price info is in the div tag

price = soup.find(name ="div",class_="ActualPrice").getText()
price = float("".join(price.split()[1].split(",")))
price = 1499
#check if the current price is less or equal than our desired price
if price <= 1500.0:
        #body of the mail
        body = "The Headphones price is now " + str(price) +", so hurry up and BUY\n LINK :" + product_url
        #send an email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection: #connect to google mail server
            connection.login(user = email,password = password)
            connection.sendmail(
                from_addr = email,
                to_addrs = "YOUR_EMAIL_ADDRESS",
                msg = 'Subject:You can buy the HEADPHONES NOW\n\n{}'.format(body) )
            print("Email Sent")
else:
    print("The price is not at the desired amount")