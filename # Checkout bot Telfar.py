# Checkout bot 
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time 
 

# def run_bot(self):
path = Service("/Users/fineas/Desktop/Coding/chromedriver_mac_arm64/chromedriver")

chrome_options = Options()

# Keep tab open after it has fully loaded
chrome_options.add_experimental_option("detach", True)

# Driver to open webpage
driver = wd.Chrome(service=path)

webpage = driver.get("https://telfar.net/collections/puff-shoppers/products/small-puff-shopper-black")

# Wait before interacting with webpage
wait = driver.implicitly_wait(7)

# Add to cart
add_to_cart = driver.find_element(By.ID, 'AddToCart')
add_to_cart.click()


# Cart navigate
go_to_cart = driver.find_element(By.XPATH, '//*[@id="shopify-section-header"]/div[2]/header/div/div[1]/div[3]/a')
driver.implicitly_wait(7)
go_to_cart.click()
go_to_cart = driver.find_element(By.XPATH, '//*[@id="shopify-section-header"]/div[2]/header/div/div[1]/div[3]/a')
go_to_cart.click()

# Wait for cart to load
wait

# Checkout 
checkout = driver.find_element(By.NAME, "checkout")
checkout.click()

# Wait for form to load
driver.implicitly_wait(7)

#Find and fill out form
email = driver.find_element(By.XPATH, '//*[@id="checkout_email"]')
email.send_keys("test@gmail.com")

first_name = driver.find_element(By.ID, "checkout_shipping_address_first_name")
first_name.send_keys("Bob")

last_name = driver.find_element(By.ID, "checkout_shipping_address_last_name")
last_name.send_keys("White")

last_name = driver.find_element(By.XPATH, '//*[@id="checkout_shipping_address_address1"]')
last_name.send_keys("5 Nowhere Ave")

city = driver.find_element(By.XPATH, '//*[@id="checkout_shipping_address_city"]')
city.send_keys("Virginia Beach")

# state = driver.find_element(By.XPATH, '//*[@id="checkout_shipping_address_province"]')
# state.click()

zip_code = driver.find_element(By.XPATH, '//*[@id="checkout_shipping_address_zip"]')
zip_code.send_keys("90011")

phone = driver.find_element(By.XPATH, '//*[@id="checkout_shipping_address_phone"]')
phone.send_keys("000-000-0000")

contin_to_ship = driver.find_element(By.XPATH, '//*[@id="continue_button"]')
contin_to_ship.click()
wait
proceed = driver.find_element(By.XPATH, '//*[@id="btn-proceed-address"]')
proceed.click()

driver.implicitly_wait(9)
continue_to_pay = driver.find_element(By.XPATH, '//*[@id="continue_button"]')
continue_to_pay.click()

wait
credit_card = driver.find_element(By.ID, 'number')
credit_card.send_keys('400030004000')




# Wait before driver is closed
time.sleep(40)

# Close driver
driver.quit()


    




