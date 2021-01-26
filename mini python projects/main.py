from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#this bot automatically submits your job application given that
    #1) Resume is already uploaded on Linkedin
    #2) Job application only requires Resume and Phone number
    #3) For 'Easy apply' applications


chrome_driver_path = "C:\Development\chromedriver.exe"
email = "your_email"
password = "your_password"
number = "your_phone_number"

url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

#click on the sign in button
signin = driver.find_element_by_link_text("Sign in")
signin.click()

#wait for page to load
#time.sleep(1)

#enter email and password
Email = driver.find_element_by_id("username")
Email.send_keys(email)

Password = driver.find_element_by_id("password")
Password.send_keys(password)

#click on sign in
signin = driver.find_element_by_css_selector(".login__form_action_container button")
signin.click()

#wait for page to load
time.sleep(2)

def Exit():
    exitt = driver.find_element_by_class_name("artdeco-modal__dismiss")
    exitt.click()

def discard():
    discard = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")
    discard[1].click()



#get all the job titles
jobs = driver.find_elements_by_class_name("job-card-container--clickable")
for job in jobs[1:]:
    job.click()

    time.sleep(2)

    #apply button
    apply = driver.find_element_by_class_name("jobs-apply-button")
    apply.click()


    #submit application
    submit = driver.find_element_by_css_selector("footer button")
    if submit.get_attribute("data-control-name") == "submit_unify":
        #enter number
        inputt = driver.find_elements_by_class_name("fb-single-line-text__input")
        #if more than 1 input field then discard
        if len(inputt) == 1:
            inputt[0].send_keys(number)
        else:
            discard()
            print("Application discarded")
        submit.click()
        print("application submitted successfully")
        time.sleep(2)
        Exit()
#if more then 1 phase to an application than discard
    else:
        Exit()
        discard()
        print("Application discarded")
    #continue_unify