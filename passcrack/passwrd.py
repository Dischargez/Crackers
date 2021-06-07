# setx path "%path%;I:\Python Lessons\Python\passcrack\geckodriver.exe"

import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox() 
driver.get("https://www.affairsandorder.com/login/")

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys("CarsonTerra")
password.send_keys("Carson226862")

driver.find_element_by_class_name("g-recaptcha").click()