from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 
import json
from os.path import exists
import py_email

driver = webdriver.Chrome(ChromeDriverManager().install())

filepath = 'hackerearth.json'

def json_create():
    
    # if exists(filepath):
    #     print("already exists")
    
    #     return 

    dictionary = {"users":[]}

    json_object = json.dumps(dictionary, indent = 4)
    
    # Writing to sample.json
    with open(filepath, "w") as outfile:
        outfile.write(json_object)

    print(dictionary)

def badges():
    badge_dict={}
    user_dict = {}
    time.sleep(3)
    profile = driver.find_element('xpath','//a[@class="track-header-profile-box"]')
    user = profile.get_attribute('href').split('/')[-1]

    print(user)
    profile.click()

    time.sleep(3)

    label = driver.find_elements('xpath','//div[@class="metric"]/div[@class="label desc-text"]')
    score = driver.find_elements('xpath','//div[@class="metric"]/div[@class="value"]')

    for i in range(len(label)):
        badge_dict[label[i].text] = score[i].text

    user_dict[user] = badge_dict

    json_create()

    with open("hackerearth.json") as f:
        data = json.load(f)

    with open("hackerearth.json","w") as of:    
        try:
            
            data ["users"].append(user_dict)
        except:
            data = {
                "users" : [user_dict]
            }
        json.dump(data,of)

    

    # print(user_dict)
    

def login(username,password1):
    driver.get('https://www.hackerearth.com/')
    driver.maximize_window()
    driver.find_element('xpath','//li[@class="login"]').click()

    user = driver.find_element('name','username')
    user.send_keys(username)
    password = driver.find_element('name','password')
    password.send_keys(password1)

    driver.find_element('xpath','//*[@class="submitButton"]').click()

    badges()

    py_email.send_email()
