# Checkout bot 
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import relative_locator as RL

import time 
 

# def run_bot(self):
path = Service("/Users/fineas/Desktop/Coding/chromedriver_mac_arm64/chromedriver")

chrome_options = Options()

# Keep tab open after it has fully loaded
chrome_options.add_experimental_option("detach", True)

# Driver to open webpage
driver = wd.Chrome(service=path)

webpage = driver.get("https://telfar.net/collections/puff-shoppers/products/small-puff-shopper-black")
# Explicitly Wait shortcut
webwait = WebDriverWait(driver, 10)
# Wait before interacting with webpage
wait = driver.implicitly_wait(7)

# Add to cart
add_to_cart = driver.find_element(By.ID, 'AddToCart')
add_to_cart.click()

# Go to cart
go_to_cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'view-cart')))
go_to_cart.click()

# Checkout 
checkout = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "checkout")))
checkout.click()

# Wait for form to load
wait

#Find and fill out form
try:
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

    # Continue to shipping confirmation page
    contin_to_ship = driver.find_element(By.XPATH, '//*[@id="continue_button"]')
    contin_to_ship.click()

    # Continue to payment page
    driver.implicitly_wait(9)
    proceed = driver.find_element(By.ID, 'continue_button')
    proceed.click()
    try:
# Fill out credit card information
    # Get all card iframes as a list
        iframes = driver.find_elements(By.CLASS_NAME, "card-fields-iframe")

        # Switch to first iframe
        driver.switch_to.frame(iframes[0])
        number = driver.find_element(By.ID, "number")
        if number.is_displayed:
            number.send_keys("4000300040005000")

        # Switch back to default frame
        driver.switch_to.default_content()
        # Switch to second iframe
        driver.switch_to.frame(iframes[1])
        name = driver.find_element(By.ID, "name")
        if name.is_displayed:
            name.send_keys("Crypto Fin")

        # Switch back to default frame
        driver.switch_to.default_content()
        # Switch to third iframe
        driver.switch_to.frame(iframes[2])
        expiry = driver.find_element(By.ID, "expiry")
        if expiry.is_displayed:
            expiry.send_keys("12")
            time.sleep(0.3)
            expiry.send_keys("2025")

        # Switch back to default frame
        driver.switch_to.default_content()
        # Switch to fourth frame
        driver.switch_to.frame(iframes[3])
        cvv = driver.find_element(By.ID, "verification_value")
        if cvv.is_displayed:
            cvv.send_keys("123")
        driver.switch_to.default_content()
    except:
        print("You Fucked Up")
    else:
        same_as_ship = driver.find_element(By.ID, "checkout_different_billing_address_false")
        if same_as_ship.is_displayed:
            same_as_ship.click()

    
finally:
    # Wait before driver is closed
    time.sleep(10)

    # Close driver
    driver.quit()


    




