from pages.items.search_item_page import SearchItemPage
from utilities.trackstatus import TrackStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import time

@pytest.mark.usefixtures("oneTimeSetUpNoLogin", "setUp")
@ddt
class SearchItemTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUpNoLogin):
        self.items = SearchItemPage(self.driver)
        self.ts = TrackStatus(self.driver)

    @pytest.mark.run(order=3)
    # * is to unpack if tuples, lists etc are used in data
    # getCSVData was mentioned in import statement above so @data recognizes it
    # Use full path + filename
    @data(*getCSVData("/Users/phuongvth/Documents/GitHub/AutomationTest-DDF/AP/testdata3.csv"))
    @unpack
    def test_searchItem(self,category):
        #click category Women
        self.items.clickCategory(category)
        time.sleep(2)
        selectItem = self.items.selectItem()
        print("Item selected: " + selectItem)
        time.sleep(2)
        self.items.searchItem(selectItem)
        time.sleep(2)
        SearchResult = self.items.getSearchResult()
        print("Item name returned: " + SearchResult)
        # if selectItem != SearchResult:
        # print("Search result")
        self.driver.back()
