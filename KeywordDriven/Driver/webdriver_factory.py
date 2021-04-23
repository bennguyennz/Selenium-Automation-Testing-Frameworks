### Download browser .exe files from selenium site###################
### Install selenium###############################

from selenium import webdriver
import os
from Utilities.Constants import Constants

class GetWebdriverInstance():

    ### Browser value is retrieved from request variable in conftest
    def __init__(self,browser):
        self.browser = browser
        self.constants = Constants()


    # Method to invoke browser based on the input from the command prompt
    def getbrowserInstance(self):
        if (self.browser == 'Firefox'):
            driver = webdriver.Firefox()
            
        # elif (self.browser == 'IE'):
        #     driver_location = self.constants.Path_IE_driver
        #     os.environ["webdriver.IE.driver"] = driver_location
        #     driver = webdriver.Ie(driver_location)

        else:
            driverLocation = self.constants.Path_Chrome_driver
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)

        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.delete_all_cookies()
        return driver


