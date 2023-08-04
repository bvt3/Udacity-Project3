# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service


# Start the browser and login with standard_user
def login (user, password):
    service = Service(executable_path="/home/devopsagent/app")
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(service=service, options=options)
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    service.stop()

login('standard_user', 'secret_sauce')

print('asdf')