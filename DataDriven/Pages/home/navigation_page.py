import Utilities.custom_logger as cl
import logging
from Base.base_page import BasePage


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _user_settings_icon = "abc"

    def navigateToUserSettings(self):
        self.elementClick(locator=self._user_settings_icon, locatorType="css")
