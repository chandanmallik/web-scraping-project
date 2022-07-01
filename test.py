
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome("/Volumes/Macintosh HD - Data/python/udemy/web_scaping_project/chromedriver")
driver.get('https://hoopshype.com/salaries/players/')
time.sleep(6)

job_title = driver.find_elements_by_xpath('//td[@class="name"]')
for i in job_title:
    print(i.text)