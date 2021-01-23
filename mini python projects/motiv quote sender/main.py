import smtplib
import random
import datetime

email = 'EMAIL_GOES_HERE'
password = 'PASSWORD_GOES_HERE'

now = datetime.datetime.now()


if now.weekday() == 1: #every Tuesday 
    with open('quotes.txt','r') as quote_file:
        quote_list = quote_file.readlines()
        quote = random.choice(quote_list)
        
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection: #connect to google mail server
        #connection.starttls() #add transport layer security
        connection.login(user = email,password = password)
        connection.sendmail(
            from_addr = email,
            to_addrs = 'recipient_address',
            msg = 'Subject:Tuesday Motivation\n\n{}'.format(quote)
    )