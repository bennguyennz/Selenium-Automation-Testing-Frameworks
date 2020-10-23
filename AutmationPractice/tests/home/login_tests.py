from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.trackstatus import TrackStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TrackStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("nguyenbinhit@yahoo.com", "1234576")
        # result1 = self.lp.verifyLoginTitle()
        # self.ts.mark(result1, "Title is incorrect")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("nguyenbinhit@yahoo.com", "1234576abc")
        result = self.lp.verifyLoginFailed()
        assert result == True

