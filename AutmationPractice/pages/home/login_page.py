
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _login_link = "Sign in"
    _email_field = "email"
    _password_field = "passwd"
    _login_button = "SubmitLogin"


    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    def login(self, email="", password=""):
        self.clickLoginLink()

        # # Scroll element into view
        # self.driver.implicitly_wait(3)
        # nail = self.driver.find_element(By.XPATH, "//h3[contains(text(),'Already registered?')]")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", nail)

        time.sleep(1)
        self.enterEmail(email)

        time.sleep(1)
        self.enterPassword(password)

        time.sleep(1)
        self.clickLoginButton()

        time.sleep(2)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//h1[contains(text(),'My account')]", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//p[contains(text(),'There is 1 error')]", locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Google")