from pages.items.checkout_item_page import CheckoutItemPage
from pages.home.navigation_page import NavigationPage
from utilities.trackstatus import TrackStatus
import unittest, pytest

import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CheckOutItemTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.items = CheckoutItemPage(self.driver)
        self.ts = TrackStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    # * is to unpack if tuples, lists etc are used in data
    # getCSVData was mentioned in import statement above so @data recognizes it
    # Use full path + filename
    def test_checkoutItem(self):
        self.items.enterItemName("Dress")
        time.sleep(0.5)
        self.items.selectItem("Blouse")
        time.sleep(0.5)
        self.items.clickOnAddtoCart()
        time.sleep(0.5)
        self.items.clickProceedtoCheckout()
        time.sleep(0.5)
        self.items.clickProceedtoCheckout_Sumary()
        time.sleep(0.5)
        self.items.clickProceedtoCheckout_Address()
        time.sleep(0.5)
        self.items.clickProceedtoCheckout_Shipping()
        time.sleep(0.5)
        self.items.clickPayByCheck()
        time.sleep(0.5)
        self.items.clickConfirm()
        time.sleep(1)
        result = self.items.verifyCompleteCheckout()
        time.sleep(3)
        self.ts.markFinal("test_checkoutItem", result,
                          "Checkout Successful Verification")

        # ALTERNATE WAY TO GO BACK USING JS:py.
        # self.driver.execute_script("window.history.go(-1)")
        self.driver.back()
