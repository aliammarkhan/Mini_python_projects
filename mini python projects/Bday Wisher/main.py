import pandas as pd
import datetime as dt
import random as rand
import numpy as np
import smtplib

email = 'YOUR_EMAIL_GOES_HERE'
password = 'YOUR_PASSWORD_GOES_HERE'


#Update the birthdays.csv
bday = pd.read_csv('birthdays.csv')



#Check if today matches a birthday in the birthdays.csv
for day,month,name,to_email in zip(bday['day'],bday['month'],bday['name'],bday['email']):
    if day == dt.datetime.now().day and month == dt.datetime.now().month:
         
         
#If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
         with open('letter_templates/letter_{}.txt'.format(rand.choice([1,2,3]))) as letter_file:
            body = letter_file.read().replace('[NAME]',name)

#Send the letter generated in step 3 to that person's email address.
         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection: #connect to google mail server
            #connection.starttls() #add transport layer security
            connection.login(user = email,password = password)
            connection.sendmail(
                from_addr = email,
                to_addrs = to_email,
                msg = 'Subject:Happy Birthday\n\n{}'.format(body) )




