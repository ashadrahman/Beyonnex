from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def goto_cart(browser):
    '''
        This function searches the cart into the page and moves
        the curser over there to click and move to the cart.
    '''
    browser.find_element(by = By.XPATH, value = ("//button[contains(text(),'Cart -')]")).click()

def click_pay_with_card(browser):
    '''
        This function finds the payment option into the cart
        and clicks it.
    '''
    browser.find_element(by = By.XPATH, value = ("//button[@type = 'submit']")).click()

def fill_cart(browser):
    '''
        This function fills the card details into the form.
    '''
    browser.switch_to.frame("stripe_checkout_app")
    browser.find_element(by = By.XPATH, value = ("//input[@type = 'email']")).send_keys("sample@gmail.com")
    sleep(1)
    
    card_number_input = browser.find_element(by = By.XPATH, value = ("//input[@placeholder = 'Card number']"))
    browser.execute_script("arguments[0].setAttribute('value', '4242424242424242')", card_number_input)
    sleep(2)
    card_date_input = browser.find_element(by = By.XPATH, value = ("//input[@placeholder = 'MM / YY']"))
    browser.execute_script("arguments[0].setAttribute('value', '11/27')", card_date_input)
    sleep(1)
    browser.find_element(by = By.XPATH, value = ("//input[@placeholder = 'CVC']")).send_keys("132")
    sleep(1)
    browser.find_element(by = By.XPATH, value = ("//input[@placeholder = 'ZIP Code']")).send_keys("2840-620")
    
    

def pay(browser):
    '''
        This function clicks over "submit" button to pay
        after filling the form and sends message whether payment
        goes successful or not.
    '''
    browser.find_element(by = By.XPATH, value = ("//*[@id='submitButton']")).click()
    
    sleep(5)
    return "success" if browser.title == "Confirmation" else "failed"
