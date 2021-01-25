from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#path to your chromedriver.exr file
chrome_driver_path = "C:\Development\chromedriver.exe"

#challenge get all the events name and dates from this link

#link to the cookie clicking game
link = "http://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(link)

#creating the updrades dictionary
upgrades_dict = {}
updgrades = driver.find_elements_by_css_selector("#rightPanel #store")[0]
upgrades = updgrades.find_elements_by_tag_name("div")
for u in upgrades:
    name = u.get_attribute("id")
    x = u.find_element_by_tag_name("b").text.split("-")
    if len(x) == 2:
        upgrades_dict[name] = int("".join(x[1].split(",")))
upgrade_keys = list(upgrades_dict.keys())
upgrade_keys.reverse()

#start the time
start = time.time()
#check for upgrades every 5 seconds
five = start + 5
#end after 5 minutes
end = start + (300) #5 minutes


clicker = driver.find_element_by_id("cookie")
#click cookie
while 1:
    clicker.click()
    #after 5 seconds check for upgrades
        #get current score
    if time.time() >= five:
        cookies_score = driver.find_element_by_id("money")
        print("score: {}".format(cookies_score.text))
        current_score = int("".join(cookies_score.text.split(",")))
            #check if any upgrade is available
        for u in upgrade_keys:
            if current_score >= upgrades_dict[u]:
                upgrade = driver.find_element_by_id(u)
                #get the upgrade
                upgrade.click()
                print("got upgrade {}".format(u))
                current_score -= upgrades_dict[u]
                break
        five+=5
    #check if 5 seconds passed
    if time.time() >= end:
        break

cookies_score = driver.find_element_by_id("cps")
print("Final score : {}".format(cookies_score.text))

#quit the browser
driver.quit()
