from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime

username = 'standard_user'
pwd = 'secret_sauce'

dt = datetime.datetime.now()
#print("Start test: ", str(dt)[0:19])

print( str(dt)[0:19] + ',Success,Start test - Starting the browser' )

o = ChromeOptions()
o.add_argument("--headless")
driver = webdriver.Chrome(options=o)
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, 'user-name').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(pwd)
driver.find_element(By.CLASS_NAME, 'submit-button').click()

dt = datetime.datetime.now()
print( str(dt)[0:19] + ',Success,Browser started successfully. Logged-in user: ' + username )

dt = datetime.datetime.now()
assert "Swag Labs" in driver.title
print( str(dt)[0:19] + ',Success,TEST PASSED: Website title' )

items = driver.find_elements(By.XPATH, '//div[@class="inventory_item"]')
for item in items:
    itemdesc = item.find_element(By.XPATH, './/div[@class="inventory_item_description"]')
    label = itemdesc.find_element(By.XPATH, './/div[@class="inventory_item_label"]')
    itemname = label.find_element(By.XPATH, './/div[@class="inventory_item_name"]')
    pricebar = itemdesc.find_element(By.XPATH, './/div[@class="pricebar"]')
    pricebar.find_element(By.CLASS_NAME, 'btn_inventory').click()
    dt = datetime.datetime.now()
    print( str(dt)[0:19] + ',Success,Added to cart: ' + itemname.text )

cartitemcount = int(driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text)
dt = datetime.datetime.now()
print( str(dt)[0:19] + ',Success,Number of items in the cart: ' + str(cartitemcount) )

assert "6" in str(cartitemcount)
print( str(dt)[0:19] + ',Success,TEST PASSED: Adding items to cart' )

driver.get('https://www.saucedemo.com/cart.html')
dt = datetime.datetime.now()
print( str(dt)[0:19] + ',Success,Navigated to the cart page' )

cartitems = driver.find_elements(By.XPATH, '//div[@class="cart_item"]')
for cartitem in cartitems:
    label = cartitem.find_element(By.XPATH, './/div[@class="cart_item_label"]')
    itemname = label.find_element(By.XPATH, './/div[@class="inventory_item_name"]')
    itemnametxt = itemname.text
    pricebar = label.find_element(By.XPATH, './/div[@class="item_pricebar"]')    
    pricebar.find_element(By.CLASS_NAME, 'cart_button').click()
    dt = datetime.datetime.now()
    print( str(dt)[0:19] + ',Success,Removed item: ' + itemnametxt )

delitemcount = 0
try:
    delitemcount = int(driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text)
except NoSuchElementException:
    delitemcount = 0

dt = datetime.datetime.now()
print( str(dt)[0:19] + ',Success,Number of items in the cart: ' + str(delitemcount) )

assert "0" in str(delitemcount)
print( str(dt)[0:19] + ',Success,TEST PASSED: Removing items to cart' )

driver.quit()

dt = datetime.datetime.now()
print( str(dt)[0:19] + ',Success,End test' )