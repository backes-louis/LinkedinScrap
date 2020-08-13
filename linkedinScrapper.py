from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from linkedinNames import list_of_names
import time
import json
import csv
import datetime

# Opening of documents to collect the data
begin_time = datetime.datetime.now()
exp = open("linkExp.txt", "w", encoding='utf-8')
fm = open("linkForm.txt", "w", encoding='utf-8')
failNam = open("linkFnames.txt", "w", encoding='utf-8')
excel = open("NameUrls.csv", "w", newline="") 
writer = csv.writer(excel)

# Login for Linkedin
# List of names to search

names_not_found = []

valid_names = []
list_of_consulted_Urls = []



i = 0
 
driver = webdriver.Chrome()
 
 
def login(driver):
    
    driver.maximize_window()
    driver.get("https://lu.linkedin.com") 
    time.sleep(2)
    #Actual Login keys 
    driver.find_element_by_id("session_key").send_keys("Louis.backes@gmail.com")
    time.sleep(3)
    driver.find_element_by_id("session_password").send_keys("Aqwzsxedc123")
    print("-----> Logging in private account...")
    time.sleep(2.5)
    driver.find_element_by_class_name("sign-in-form__submit-button").click()
    time.sleep(4)
    print("-----> Login Done...")
    time.sleep(1)
 
def search(driver):
    
    driver.get("https://www.google.com/?hl=fr")
    print("-----> On Google...")
    driver.find_element_by_name("q").send_keys(list_of_names[i] + " Linkedin")
    print("-----> Retrieved the name " + list_of_names[i] + "...")
    
    time.sleep(3)
    driver.find_element_by_name("q").send_keys(Keys.RETURN)
    time.sleep(2.5)
    
    url_linkedin = driver.find_element_by_class_name("r")
    try:
        url_linkedin == False
    except:
        print("-----> No such name was found " + list_of_names[i] + "...")
        time.sleep(2)
        return None
    else:
        url_linkedin.click()
        print("-----> Logging in on Profile: " + list_of_names[i] + "...")
        time.sleep(5)

def getFormation():
    time.sleep(2)
    try:
        formation_section = driver.find_element_by_id("education-section")
    except:
        print("-----> No Formation section for " + list_of_names[i] + " was Found...")
        
        return None
    
    else:
        formation_data = formation_section.text
        print("-----> Formation Data Gathered...")
        time.sleep(1)
        print("-----> Writing Formation Data in file...")
        fm.write("\n" + list_of_names[i] + " ----> Formation:" + "\n" + formation_data + "\n")
        
        
        
    return formation_data

def getExperience():
    
    time.sleep(2)
    try:
        experience_section = driver.find_element_by_id("experience-section")

    except:
        print("-----> No experience section for " + list_of_names[i] + " was Found...")
        return None
        
    else:
        data = experience_section.text
        print("-----> Experience Data gathered...") 
        exp.write(list_of_names[i] + "\n" + "\n" + data + "\n")
        valid_names.append("".join(list_of_names[i]))
        Urls = driver.current_url
        list_of_consulted_Urls.append("".join(Urls))
        print("-----> Writing Data in file...")
    
    return data

def endDriver():
    print("-----> Closing Driver...")
    driver.quit()
 
login(driver)
for names in list_of_names:
    search(driver)
    
    if getFormation() == None:
        time.sleep(2)

    if getExperience() == None:
        time.sleep(2)
        names_not_found.append("".join(list_of_names[i]))

    
    time.sleep(2.5) 
    i += 1

endDriver()



writer.writerow(["Names", "Consulted Urls"])
writer.writerows(zip(valid_names, list_of_consulted_Urls))
for noName in names_not_found:
    json.dump(names_not_found, failNam)

failNam.close()
fm.close()
exp.close()

print(datetime.datetime.now() - begin_time)
