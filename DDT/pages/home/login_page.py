
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
        time.sleep(1)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)
        time.sleep(2)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)
        time.sleep(2)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")
        time.sleep(2)

    def login(self, email="", password=""):
        self.clickLoginLink()
        # self.driver.implicitly_wait(3)
        # nail = self.driver.find_element(By.XPATH, "//h3[contains(text(),'Already registered?')]")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", nail)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()


    def verifyLoginSuccessful(self):
        time.sleep(2)
        result = self.isElementPresent("//h1[contains(text(),'My account')]", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        time.sleep(2)
        result = self.isElementPresent("//p[contains(text(),'There is 1 error')]", locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Google")

