from pages.items.checkout_item_page import CheckoutItemPage
from pages.home.navigation_page import NavigationPage
from utilities.trackstatus import TrackStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
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
    @data(*getCSVData("/Users/phuongvth/Documents/GitHub/AutomationTest-DDF/DataDriven/testdata2.csv"))
    @unpack
    def test_checkoutItem(self,search_keyword,item_name,size,color):
        self.items.enterSearchKeyword(search_keyword)
        time.sleep(0.5)
        self.items.selectItem(item_name)
        time.sleep(0.5)
        self.items.clickOnAddtoCart(size,color)
        time.sleep(1)
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
        time.sleep(1)
        self.ts.markFinal("test_checkoutItem", result,
                          "Checkout Successful Verification")
######################
        # ALTERNATE WAY TO GO BACK USING JS:py.
        # self.driver.execute_script("window.history.go(-1)")
        self.driver.back()
