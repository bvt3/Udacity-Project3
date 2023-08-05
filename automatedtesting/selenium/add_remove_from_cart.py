from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime

username = 'standard_user'
pwd = 'secret_sauce'

dt = datetime.datetime.now()
print("Start test: ", dt)

print ('Starting the browser...')
o = ChromeOptions()
o.add_argument("--headless")
driver = webdriver.Chrome(options=o)
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, 'user-name').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(pwd)
driver.find_element(By.CLASS_NAME, 'submit-button').click()

print ('Browser started successfully. Logged-in user: ' + username + '.')

items = driver.find_elements(By.XPATH, '//div[@class="inventory_item"]')
for item in items:
    itemdesc = item.find_element(By.XPATH, './/div[@class="inventory_item_description"]')
    label = itemdesc.find_element(By.XPATH, './/div[@class="inventory_item_label"]')
    itemname = label.find_element(By.XPATH, './/div[@class="inventory_item_name"]')
    pricebar = itemdesc.find_element(By.XPATH, './/div[@class="pricebar"]')
    pricebar.find_element(By.CLASS_NAME, 'btn_inventory').click()
    print('Added to cart: ' + itemname.text)

cartitemcount = int(driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text)
print('Number of items in the cart: ' + str(cartitemcount))

driver.get('https://www.saucedemo.com/cart.html')
print('Navigated to the cart page')

cartitems = driver.find_elements(By.XPATH, '//div[@class="cart_item"]')
for cartitem in cartitems:
    label = cartitem.find_element(By.XPATH, './/div[@class="cart_item_label"]')
    itemname = label.find_element(By.XPATH, './/div[@class="inventory_item_name"]')
    itemnametxt = itemname.text
    pricebar = label.find_element(By.XPATH, './/div[@class="item_pricebar"]')    
    pricebar.find_element(By.CLASS_NAME, 'cart_button').click()
    print('Removed item: ' + itemnametxt)

delitemcount = 0
try:
    delitemcount = int(driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text)
except NoSuchElementException:
    delitemcount = 0

print('Number of items in the cart: ' + str(delitemcount))

if cartitemcount == 6 and delitemcount == 0:
    print("Test passed!")
else:
    print("Test failed!")

driver.quit()

dt = datetime.datetime.now()
print("End test: ", dt)