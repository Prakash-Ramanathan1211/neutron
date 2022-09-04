from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 
import json
from os.path import exists

driver = webdriver.Chrome(ChromeDriverManager().install())

filepath = 'hackerrank.json'

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

def submissions(username):
    user_dict = {}
    sub_dict = {}
    flag = True

    while flag:
        time.sleep(3)

        problem = driver.find_elements('xpath','//a[@data-analytics="ChallengeViewSubmChallengeName"]')
        score = driver.find_elements('xpath','//div[@class="span1"]/p[@class="small"]')

        # print(sub_dict)

        for i in range(len(problem)):
            sub_dict[problem[i].text] = float(score[i].text )

        try:
            driver.find_element('xpath','//li[@class="disabled"]/a[@data-attr1="Right"]')
            flag=False
            # break
        except:
            time.sleep(2)
            driver.find_element('xpath','//li/a[@data-attr1="Right"]').click()

    user_dict[username] = sub_dict

    print(user_dict)

    with open("hackerrank.json") as f:
        data = json.load(f)

    with open("hackerrank.json","w") as of:    
        try:
            
            data ["users"].append(user_dict)
        except:
            data = {
                "users" : [user_dict]
            }
        json.dump(data,of)

def login(username,password1):
    # driver.get('https://www.hackerrank.com/')
    # login1 = driver.find_element('xpath','//a[@data-event-action="Login"]')
    # login1.click()

    # login2 = driver.find_element('xpath','//*[@class="fl-button-wrap fl-button-width-auto fl-button-left"]/a')
    # login2.click()

    driver.get('https://www.hackerrank.com/auth/login')
    
    user = driver.find_element('id','input-1')
    user.send_keys(username)

    password = driver.find_element('id','input-2')
    password.send_keys(password1)

    driver.find_element('xpath','//button[@data-analytics="LoginPassword"]').click()

    time.sleep(3)

    driver.find_element('xpath','//div[@data-analytics="NavBarProfileDropDown"]').click()

    driver.find_element('xpath','//a[@data-analytics="NavBarProfileDropDownSubmissions"]').click()

    username = driver.find_element('xpath','//*[@class="mmR profile-username"]').text

    json_create()

    submissions(username)


# if __name__ == "__main__":
#     login()