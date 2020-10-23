import utilities.custom_logger as cl
import logging
from base.base_page import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _search_box = "search-courses"
    # {0} is a placeholder and the actual value that will be used is passed in by .format()
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "course-listing-title"
    _enroll_button = "enroll-button-top"
    _cc_num = "cardnumber"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _zip = "postal"
    _enroll_disabled = "//div[@class='spc__primary-submit is-disabled']"
    _search_button = "search-course-button"

    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box)

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def clickSearchButton(self):
        self.elementClick(locator=self._search_button)

    def enterCardNum(self, num):
        self.driver.switch_to.frame("__privateStripeFrame4")
        self.sendKeys(num, self._cc_num, locatorType="name")
        self.driver.switch_to.default_content()

    def enterCardExp(self, exp):
        self.driver.switch_to.frame("__privateStripeFrame5")
        self.sendKeys(exp, self._cc_exp, locatorType="name")
        self.driver.switch_to.default_content()

    def enterCardCVV(self, cvv):
        self.driver.switch_to.frame("__privateStripeFrame6")
        self.sendKeys(cvv, self._cc_cvv, locatorType="name")
        self.driver.switch_to.default_content()

    def enterZip(self, zip):
        self.driver.switch_to.frame("__privateStripeFrame7")
        self.sendKeys(zip, self._zip, locatorType="name")
        self.driver.switch_to.default_content()

    def enterCreditCardInformation(self, num, exp, cvv, zip):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterZip(zip)

    # Make parameters optional so that we can test without any/all of them for invalid scenarios
    def enrollCourse(self, num="", exp="", cvv="", zip=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv, zip)

    def verifyEnrollFailed(self):
        result = self.isElementPresent(self._enroll_disabled, locatorType="xpath")
        return result
