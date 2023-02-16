from selenium import webdriver
from getpass import getpass
from selenium.webdriver.chrome.options import Options
import time
import pickle
chrome_options = Options()


username=input("IEMB Username:") #Gets User IEMB


password=input("IEMB Password:") #Gets User PW


chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome("/usr/local/bin/chromedriver",chrome_options=chrome_options) #Opens Chromedriver on mac, but must change path on win
driver.get("https://iemb.hci.edu.sg/") #Goes to iemb


username_textbox = driver.find_element_by_id("UserName") #Selenium Finds input user box
username_textbox.send_keys(username) # Selenium sends ur user

password_textbox = driver.find_element_by_id("Password") #Selenium Finds input pw box
password_textbox.send_keys(password) # Selenium sends ur pw

login_button = driver.find_element_by_id("submitbut")#Selenium Finds submit form
login_button.submit() #Selenium submits form

time.sleep(2) #Delay, in case of lag (Can Change)

click_button = driver.find_element_by_xpath('//a[@href="/Board/Detail/1048"]') #Finds Redirect Element to our board
driver.execute_script("arguments[0].click();", click_button) #Presses button

time.sleep(2)#Delay, in case of lag (Can Change)

with open ("ok.txt", "w") as f:
    f.write(driver.page_source) #Selenium saves html of website into ok.txt


c= driver.get_cookies()    #Selenium saves all browser login cookines into cookies.txt
with open('cookies.txt', 'w') as file:
    file.write(str(c))

driver.close()   #Selenium closes, so ur pc doesnt explode haha ok
