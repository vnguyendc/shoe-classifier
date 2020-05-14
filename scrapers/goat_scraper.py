import os
import time
from selenium import webdriver

url = 'https://www.goat.com/sneakers'

driver = webdriver.Chrome('/Users/vinhnguyen/Documents/DataScience/shoe-classifier/chromedriver')
driver.get(url)
driver.implicitly_wait(3)

# clicks `show more` to get more shoes
for i in range(3):
    time.sleep(3)
    #driver.find_element_by_link_text('Apparel').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/div[5]/div[1]/div[2]/div[3]/div/button').click()
    print('Clicked "Show More"')

names = []
image_urls = []
