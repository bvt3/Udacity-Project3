# # #!/usr/bin/env python
# from selenium import webdriver
# #from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.chrome.service import Service


# # Start the browser and login with standard_user
# def login (user, password):
#     caps = {}
#     caps['browserName'] = 'chrome'

#     service = Service(executable_path="/home/devopsagent/app")
#     print ('Starting the browser...')
#     # --uncomment when running in Azure DevOps.
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless") 
#     # driver = webdriver.Chrome(options=options)
#     #driver = webdriver.Chrome()
#     driver = webdriver.Chrome(service=service, options=options)
#     print ('Browser started successfully. Navigating to the demo page to login.')
#     driver.get('https://www.saucedemo.com/')
#     service.stop()

# login('standard_user', 'secret_sauce')

# print('asdf')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time import sleep


# Set options for not prompting DevTools information
o = Options()
#o.add_experimental_option("excludeSwitches", ["enable-logging"])
o.add_argument("--headless") 
o.set_capability("browserName", "chrome")

print("testing started")
driver = webdriver.Chrome(options=o)
driver.get("https://www.saucedemo.com/")
sleep(1)

# Get page title
title = driver.title

# Test if title is correct
assert "Swag Labs" in title
print("TEST 0: `title` test passed")

# Close the driver
driver.quit()