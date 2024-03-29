import Utilities.custom_logger as cl
import logging
from Base.base_page import BasePage
from Pages.home.navigation_page import NavigationPage
import time


# Inherit from BasePage class
class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    # Call super constructor and pass driver.  Need driver for LoginPage too.
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    # _login_link = "Login"
    # _email_field = "user_email"
    # _password_field = "user_password"
    # _login_button = "commit"
    _login_link = "Sign in"
    _email_field = "email"
    _password_field = "passwd"
    _login_button = "SubmitLogin"
    _successful_validation = "//p[@class='info-account']"
    _unsuccessful_validation = "//p[contains(text(),'There is 1 error')]"

    # The custom elementClick and sendKeys methods locate the element then perform the action on the element
    # sendKeys is the custom method, not send_keys
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")
        return True

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)
        return True

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)
        return True

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")
        return True

    def login(self, email="", password=""):

        self.clickLoginLink()
        time.sleep(1)
        self.log.info("Wait for a while")
        self.webScroll()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(1)
        self.log.info("Wait for a while")

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(locator=self._successful_validation,
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator=self._unsuccessful_validation,
                                       locatorType="xpath")
        return result

    def clearLoginFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Google")

    def logout(self):
        #self.nav.navigateToUserSettings()
        self.elementClick(locator="Sign out",
                          locatorType="link")
