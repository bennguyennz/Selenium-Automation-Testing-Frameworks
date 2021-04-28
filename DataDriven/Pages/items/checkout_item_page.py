import Utilities.custom_logger as cl
import logging
from Base.base_page import BasePage
from selenium.webdriver.support.select import Select
from traceback import print_stack


class CheckoutItemPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _search_box = "search_query_top"
    # {0} is a placeholder and the actual value that will be used is passed in by .format()
    _search_box_button = "submit_search"
    _item_name = "//a[@title='{0}'][normalize-space()='{0}']"
    _dropdown_list = "group_1"
    _size = "0"
    _choose_color = "//a[@name='{0}']"
    _add_to_cart_button = "//span[contains(text(),'Add to cart')]"
    _proceed_to_checkout_button = "//span[normalize-space()='Proceed to checkout']"
    _proceed_to_checkout_summary = "div#center_column  a[title='Proceed to checkout'] > span"
    _process_address_button = "processAddress"
    _checkbox = "cgv"
    _process_carrier_button = "processCarrier"
    _pay_button = "cheque"
    _confirm_button = "p#cart_navigation  span"
    _validation_success = "//button[@name='submit_search']"


    ############################
    ### Element Interactions ###
    ############################

    def enterSearchKeyword(self, name):

        self.sendKeys(name, locator=self._search_box)
        self.elementClick(locator=self._search_box_button, locatorType="name")

    def selectItem(self, ItemName):
        try:
            if self.getElement(locator=self._item_name.format(ItemName),locatorType="xpath"):
                self.elementClick(locator=self._item_name.format(ItemName), locatorType="xpath")
                self.webScroll()
                return True
        except:
            self.log.info("Item not found with locator " + self._item_name.format(ItemName) + " and locatorType xpath")
            return False

    def clickOnAddtoCart(self,_size="", _color=""):
        dropdownlist = Select(self.getElement(locator = self._dropdown_list))
        dropdownlist.select_by_visible_text(format(_size))
        self.elementClick(locator = self._choose_color.format(_color), locatorType = "xpath")
        self.elementClick(locator = self._add_to_cart_button, locatorType = "xpath")
        return True

    def clickProceedtoCheckout(self):
        self.elementClick(locator = self._proceed_to_checkout_button,locatorType = "xpath")
        return True

    def clickProceedtoCheckout_Sumary(self):
        self.elementClick(locator=self._proceed_to_checkout_summary,locatorType="css")
        return True

    def clickProceedtoCheckout_Address(self):
        self.elementClick(locator=self._process_address_button,locatorType="name")
        return True

    def clickProceedtoCheckout_Shipping(self):
        self.elementClick(locator=self._checkbox)
        self.elementClick(locator=self._process_carrier_button,locatorType="name")
        return True

    def clickPayByCheck(self):
        self.elementClick(locator=self._pay_button,locatorType="class")
        return True

    def clickConfirm(self):
        self.elementClick(locator=self._confirm_button,locatorType="css")
        return True

    def verifyCompleteCheckout(self):
        self.webScroll()
        self.isElementPresent(locator=self._validation_success, locatorType="xpath")
        return True
