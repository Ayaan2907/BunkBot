import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from parameters import *
# command to start chrome in debug mode google-chrome --remote-debugging-port=0908

print("Started...")
chromeOptions = Options()
# chromeOptions.add_experimental_option("debuggerAddress","localhost:0908")
browser = webdriver.Chrome(options=chromeOptions)
print("Sessioned opened.")
url = "https://teams.microsoft.com/_#/calendarv2"
# url = "https://teams.microsoft.com/"
browser.get(url)
initialCounter = time.perf_counter()
print("URL reached.")

def frequentErr(id, name):
    while True:
        try:
            parameter=browser.find_element_by_id(id)
            print(f"...try for {name}")
            return parameter
        except selenium.common.exceptions.NoSuchElementException as err:
            print(f"...for {name} > excepting {err}")
            time.sleep(5)

def JoinTeams(emailid, password):

    email=browser.find_element_by_id("i0116")
    email.send_keys(emailid)
    time.sleep(1.5)
    print("Email entered!")
    frequentErr("idSIButton9", "Email-Submit-Button" ).click()

    passwd=browser.find_element_by_id("i0118")
    passwd.send_keys(password)
    time.sleep(1.5)
    print("Password entered!")
    frequentErr("idSIButton9", "Password-Submit-Button" ).click()

    time.sleep(1.5)
    confirmbtn=browser.find_element_by_id("idSIButton9")
    print("Confirming...!")
    confirmbtn.click()
    # time.sleep(1.5)
    print("Logged in...!")
    time.sleep(1.5)
    # try:
    #     # web_appBtn = browser.find_elements_by_class_name("use-app-lnk")
    #     web_appBtn=browser.find_element_by_link_text("Use the web app instead")
    #     web_appBtn.click()
    #     print("Opening web-app.")
    # except selenium.common.exceptions.NoSuchElementException as err:
    #     print("excepting")
    # time.sleep(1.5)
    # time.sleep(1.5)
    # frequentErr("app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c", "Calender-Button").click()
    finalCounter = time.perf_counter()   
    print(f"TEAMS web-app loaded {finalCounter - initialCounter:0.2f} seconds")
    

def SignoutTeams():
    time.sleep(5)
    frequentErr("personDropdown", "Profile-DropDown-Button" ).click()
    time.sleep(1.5)
    frequentErr("logout-button", "Logout-Button").click()


JoinTeams(CONST_userName, CONST_loginPassword)
time.sleep(5)
SignoutTeams()



