from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window() 

driver.get("https://www.thesparksfoundationsingapore.org/")
elem = bool
elem=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/h1/a/img")
if elem:
    print("Logo Exist in Homepage")
else:
    print("Logo Missing from Homepage")

time.sleep(2)
driver.quit()
print ("The test is completed")