from selenium.webdriver.common.by import By
def temperature_finder(browser):
    '''
        This function finds the temperature by
        scraping the page
    '''
    temperature = browser.find_element(By.ID,"temperature")
    return int(temperature.text[:-2])
