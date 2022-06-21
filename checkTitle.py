from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window() 

driver.get("https://www.thesparksfoundationsingapore.org/")
title=driver.title;
if title=="The Sparks Foundation | Home":
    print("Page Title name is correct")
else:
    print("Wrong Title Name")


print ("The test is completed")
driver.close()