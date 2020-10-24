import utilities.custom_logger as cl
import logging
from base.base_page import BasePage
from pages.home.navigation_page import NavigationPage
from selenium.webdriver.common.by import By
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

    # The custom elementClick and sendKeys methods locate the element then perform the action on the element
    # sendKeys is the custom method, not send_keys
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
        time.sleep(1)
        nail = self.driver.find_element(By.XPATH, "//h3[contains(text(),'Already registered?')]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", nail)
        self.enterEmail(email)
        time.sleep(1)
        self.enterPassword(password)
        time.sleep(1)
        self.clickLoginButton()
        time.sleep(1)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//h1[contains(text(),'My account')]",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//p[contains(text(),'There is 1 error')]",
                                       locatorType="xpath")
        return result

    def clearLoginFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Kode")

    def logout(self):
        self.nav.navigateToUserSettings()
        self.elementClick(locator="Sign out",
                          locatorType="link")
