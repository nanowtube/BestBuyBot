# Imports stealth
from selenium_stealth import stealth
# Python's built in time module
import time
# Python's built-in random module
import random
# imports webdriver
from selenium import webdriver
# WebDriverWait waits for the element to be present on the page and acts upon it
from selenium.webdriver.support.wait import WebDriverWait
# Select is used for elements in the dropdown manu
from selenium.webdriver.support.ui import Select
# NoSuchElementException occurs when the element is not present to be selected
from selenium.common.exceptions import NoSuchElementException
# Defined conditions to use with WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Selecting elements using By
from selenium.webdriver.common.by import By
# Keys is used to mimick key presses within Selenium
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
# Configurations for selenium driver
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--profile-directory=Person 4")
opt.add_experimental_option('useAutomationExtension', False)
opt.add_argument("disable-popup-blocking")
driver = webdriver.Chrome(options=opt)
# Calls and configure Selenium stealth using OpenGL
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

driver.get("https://www.bestbuy.com/site/logitech-c920s-pro-1080p-webcam-with-privacy-shutter-black/6321794.p?skuId=6321794")
foundButton = False
time.sleep(5)

# While loop looks for add to cart button and refreshes page until found
while not foundButton:
    addToCartButton = addButton = driver.find_element_by_class_name(
        "add-to-cart-button")

    if ("c-button-disabled" in addToCartButton.get_attribute("class")):
        time.sleep(30)

        # reload page
        driver.refresh()
    else:
        # button is found and while loop is exited
        foundButton = True
# Clicks add to cart button
addToCartButton.click()

# Waits up to 120 seconds for the element to be found, looking for element based on Link Text
goToCart = WebDriverWait(driver, 120).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Go to Cart")))
goToCart.click()
# Waits up to 120 seconds for the element to be found, looking for element based on CSS selector
shipping = WebDriverWait(driver, 120).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[id*='fulfillment-shipping']")))
shipping.click()
# Randomizes wait time to appear more human
time.sleep(random.uniform(0, 3))
# Finds checkout button element based on class name
checkoutBtn = driver.find_element_by_class_name("btn-primary")
checkoutBtn.click()
# Waits up to 120 seconds for the element to be found, looking for element based on class name
continueAsGuest = WebDriverWait(driver, 120).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "guest")))
continueAsGuest.click()
# Waits up to 120 seconds for the element to be found, looking for element based on name
firstName = WebDriverWait(driver, 120).until(
    EC.element_to_be_clickable((By.NAME, "firstName")))

# Types in each character at a random interval, makes input more human-like
for i in "Bucko":
    firstName.send_keys(i)
    time.sleep(random.uniform(0, 0.5))
# Looks for last name field by searching for the element by name
lastName = driver.find_element_by_name("lastName")
# Types in each character at a random interval, makes input more human-like
for i in "Slim":
    lastName.send_keys(i)
    time.sleep(random.uniform(0, 0.5))
time.sleep(1)
# Looks for street field by searching for the element by name
street = driver.find_element_by_name("street")
# Types in each character at a random interval, makes input more human-like
for i in "2008 Wen":
    street.send_keys(i)
    time.sleep(random.uniform(0, 0.5))
# Looks for the autocomplete by searching for the element by class name
auto = driver.find_element_by_class_name('tb-input.autocomplete__input')
# Keys down and selects the first autocomplete result
auto.send_keys(Keys.ARROW_DOWN)
time.sleep(random.uniform(0, 3))
auto.send_keys(Keys.ENTER)
time.sleep(random.uniform(0, 3))
time.sleep(3)
# Looks for the apply information button by finding the element by class name
apply = driver.find_element_by_class_name(
    'c-button.c-button-secondary.c-button-md.new-address-form__button')
apply.click()
time.sleep(3)
# looks for email address textbox by finding the emailAddress element by id
emailAddress = driver.find_element_by_id("user.emailAddress")
emailAddress.send_keys("thebestbuybot@protonmail.com")
# looks for phone textbox by finding the phone element by id
phone = driver.find_element_by_id("user.phone")
phone.send_keys("3048990040")
# finds the pay button by finding the element based on the class name
payInfoButton = driver.find_element_by_class_name("button--continue")
payInfoButton.click()
time.sleep(5)
# finds the card number textbox by finding the number element by id
cardInfo = driver.find_element_by_id("number")
cardInfo.send_keys("4737029888253631")
time.sleep(3)
# tries to select element in dropdown menu by id using expMonth, if it throws an expection select by expiration-month
try:
    selectMonth = Select(driver.find_element_by_id("expMonth"))
except NoSuchElementException:
    selectMonth = Select(driver.find_element_by_name("expiration-month"))
selectMonth.select_by_visible_text("04")
# tries to select element in dropdown menu by id using expiration-year, if it throws an expection select by expYear
try:
    selectYear = Select(driver.find_element_by_name("expiration-year"))
except NoSuchElementException:
    selectYear = Select(driver.find_element_by_name("expYear"))
selectYear.select_by_visible_text("2028")
# tries to find element by the id credit-card-cvv, if not present select by id cvv
try:
    cardCVV = driver.find_element_by_id("credit-card-cvv")
except NoSuchElementException:
    cardCVV = driver.find_element_by_id("cvv")
cardCVV.send_keys("818")
# Clicks the finish pay button when it becomes available
finishPay = WebDriverWait(driver, 120).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
finishPay.click()
# waits for confirmation (60 seconds)
time.sleep(60)
# Quits driver
driver.quit()
