from Pages.home.login_page import LoginPage
from Utilities.trackstatus import TrackStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from Utilities.read_data import getCSVData


# Use oneTimeSetUp and setUp from conftest
@ddt
@pytest.mark.usefixtures("oneTimeSetUpNoLogin", "setUp")
class LoginTests(unittest.TestCase):

    # classSetup creates the Login Page object.  This method is different than the conftest setUp method
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUpNoLogin):
        self.lp = LoginPage(self.driver)
        self.ts = TrackStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/phuongvth/Documents/GitHub/AutomationTest-DDF/DataDriven/testdata1a.csv"))
    @unpack
    def test_validLogin(self, email, password):
        self.lp.login(email, password)
        resultValidLogin = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", resultValidLogin, "Login was successful")

    @pytest.mark.run(order=2)
    @data(*getCSVData("/Users/phuongvth/Documents/GitHub/AutomationTest-DDF/DataDriven/testdata1b.csv"))
    @unpack
    def test_invalidLogin(self, email, password):

        self.lp.logout()
        self.lp.login(email, password)
        resultInvalidLogin = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin", resultInvalidLogin, "Check invalid Login")
