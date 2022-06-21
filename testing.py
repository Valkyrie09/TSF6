from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()  

driver.get("https://www.google.com/")  

driver.find_element_by_name("q").send_keys("sparks foundation")  
time.sleep(3)  
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
time.sleep(3)  
print("sample test case successfully completed") 
