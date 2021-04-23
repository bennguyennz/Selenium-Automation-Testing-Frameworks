from Pages.items.checkout_item_page import CheckoutItemPage
from Pages.home.navigation_page import NavigationPage
from Utilities.trackstatus import TrackStatus
import unittest, pytest
from ddt import ddt, data, unpack
from Utilities.read_data import getCSVData
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class CheckOutItemTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.items = CheckoutItemPage(self.driver)
        self.ts = TrackStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=4)
    # * is to unpack if tuples, lists etc are used in data
    # getCSVData was mentioned in import statement above so @data recognizes it
    # Use full path + filename
    @data(*getCSVData("/Users/phuongvth/Documents/GitHub/AutomationTest-DDF/DataDriven/testdata3.csv"))
    @unpack
    def test_checkoutItem(self, search_keyword, item_name, size, color):
        self.items.enterSearchKeyword(search_keyword)
        self.items.selectItem(item_name)
        self.items.clickOnAddtoCart(size,color)
        time.sleep(1)
        self.items.clickProceedtoCheckout()
        self.items.clickProceedtoCheckout_Sumary()
        self.items.clickProceedtoCheckout_Address()
        self.items.clickProceedtoCheckout_Shipping()
        self.items.clickPayByCheck()
        self.items.clickConfirm()
        result = self.items.verifyCompleteCheckout()
        time.sleep(1)
        self.ts.markFinal("test_checkoutItem", result,
                          "Checkout Successful Verification")
######################
        # ALTERNATE WAY TO GO BACK USING JS:py.
        # self.driver.execute_script("window.history.go(-1)")
        self.driver.back()
