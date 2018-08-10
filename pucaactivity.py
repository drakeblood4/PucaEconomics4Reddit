import json
import string
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup, SoupStrainer


DRIVER = webdriver.Firefox(executable_path='/Users/nobody/Downloads/geckodriver')

DRIVER.get("http://pucatrade.com/login")

try:
    with open('pu_data.json') as json_data:
        save = json.load(json_data)
except:
    save = {}


while(1):
    if DRIVER.current_url == "https://pucatrade.com/nexus":
        break

while(1):
    #print(len(save))
    for i in range (1,41):
        randy = random.randint(1,186878)

        try:
            x = (save[str(randy)])
            print ("Birthday Paradox: %i" % randy)
            print("GOT HERE YOU FUCKBOIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
            continue
        except:
            pass
        
        
        gotostring = "https://pucatrade.com/profiles/wants/" + str(randy)
        DRIVER.get(gotostring)

        
        failed = 0
        premium = 0
        uncommon = 0
        rare = 0
        value = 0
        reason = []
        country = 'none'
        most_recent_want_update = 0
        account_type = 0
        sent = 0
        cards = []
        
        
        if (DRIVER.current_url == "https://pucatrade.com/nexus"
            or DRIVER.current_url == "https://pucatrade.com/"):
            #print("User %i: Deleted, Banned, or Private" % randy)
            failed = 1
            reason.append("deleted")
        else:
            
            soup = BeautifulSoup(DRIVER.page_source, "lxml")
            
            titles = soup.find_all(class_="main-title")
            sent = titles[2].text

            if len(soup.find_all(class_="icon-puca-rare")) != 0:
                premium = 1
                rare = 1

            if len(soup.find_all(class_="icon-puca-uncommon")) != 0:
                premium = 1
                uncommon = 1
                
                

            price = soup.find_all(class_="price undefined")
            value = price[0].text
            value = str(value) #this is ever so slightly dangerous but I'm lazy
            value = value.translate(None, string.punctuation)
            value = int(value)

            wants1 = soup.find_all(class_= "item clear animated")
            #print(len(wants1))
            wants2 = soup.find_all(class_="item clear animated promoted")
            #print(len(wants2))
            wants = wants1 + wants2
            

                

            date = 0
            if len(wants) > 0:
                date = wants[0].find_all(class_= "column date")
                date = str(date)
                date = date[-11:-7]
                date = int(date)
                #print(date)

            icons = soup.find_all(class_= "icon")
            country = icons[10]['class'][1]
            country = str(country)
            country = country[-2:]
            #print(country)
                
                

        
            
    ##        if value <= 600:
    ##            print("User %i: Zeroed Out Account" % randy)
    ##            failed = 1
                
            if sent[0] == "0":
                #print("User %i: Never Traded" % randy)
                failed = 1
                reason.append("never traded")
                
            if len(wants) == 0:
                #print("User %i: No Wants" % randy)
                failed = 1
                reason.append("no wants")
            if date != 2018:
                if date != 0:
                    print(date)
                #print("User %i: Wants not updated since last year" % randy)
                failed = 1
                reason.append("wants not updated since last year")

                       
        if failed == 0:
            #print("User %i: Active User" % randy)
            pass

        save[str(randy)] = {"failed": failed,
                            "value": value,
                            'reason':list(reason),
                            'country':country,
                            'premium':premium,
                            'rare':rare,
                            'uncommon':uncommon}

        

##        ActiveUserPercent = 1.0-(fails/i)
##        ActiveUserPercent *= 100

##        if i % 10 == 0:
##            print("Number of users checked: %i" % i)
##            print("Active User Percentage: %f%%" % ActiveUserPercent)
    print('finished a loop of 40')
    with open('pu_data.json', 'w') as outfile:
        json.dump(save, outfile)
