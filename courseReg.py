#Code by Bradon Soucy 4/19/2023
#Auto Course Registration Tool:

#imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time

# Open Python controlled Chrome Browser
driver = webdriver.Chrome()
n = len(sys.argv)

#Go to course reg page
driver.get('https://aisweb1.uvm.edu/pls/owa_prod/bwskfreg.P_AltPin')

#Sign in using user's entered ID and password
driver.find_element(By.ID, 'UserID').send_keys(sys.argv[1])
driver.find_element(By.ID, 'PIN').send_keys(sys.argv[2])
driver.find_element(By.XPATH, "//input[@value = 'Login']").click()

#Now that the user is logged in, go to the course reg page again
driver.get('https://aisweb1.uvm.edu/pls/owa_prod/bwskfreg.P_AltPin')
driver.find_element(By.XPATH, "//input[@value = 'Submit']").click()


#Check to see if the registration page has opened by spamming this button
#Once this button no longer exists that means we are in
while(True):
    try:
        driver.find_element(By.LINK_TEXT, "Check Registration Availability Again").click()
    except:
        break;

#Now loop through the entered class codes and enter them in the desginated fields and hit submit.
for i in range(3,n):
    ids = "//input[@id = 'crn_id" + str(i-2) + "']"
    driver.find_element(By.XPATH, ids).send_keys(sys.argv[i])
driver.find_element(By.XPATH,"//input[@value = 'Submit Changes']").click()


#Keeps the browser open so we can see the status of our classes
#(Rather then closing the browser immediately)
time.sleep(5000)
