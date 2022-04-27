from selenium import webdriver
from selenium.webdriver.common import keys
import csv

from selenium import webdriver
from selenium.webdriver.common import keys
import csv


driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.get('https://amazon.com')

with open("amazon_cookies.csv") as f:
    print(f.read())
    dict_reader = csv.DictReader(f)
    cookies = list(dict_reader)


for i in cookies:
    driver.add_cookie(i)
    


driver.refresh()


# print(driver.get_cookies())

