from Pages.items.search_item_page import SearchItemPage
from Utilities.trackstatus import TrackStatus
import unittest, pytest
from ddt import ddt, data, unpack
from Utilities.read_data import getCSVData
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
    @data(*getCSVData("/Users/phuongvth/Documents/GitHub/AutomationTest-DDF/DataDriven/testdata2.csv"))
    @unpack
    def test_searchItem(self,category,itemSearch):
        #click category Women
        resutlStep1 = self.items.clickCategory(category)
        self.ts.mark(resutlStep1,"Click a Category")
        time.sleep(1)
        resultStep2 = self.items.selectItem(itemSearch)
        self.ts.mark(resultStep2[1],"Select item with name: " + resultStep2[0] )
        time.sleep(1)
        resultStep3 = self.items.searchItem(resultStep2[0])
        self.ts.mark(resultStep3,"Search item")

        time.sleep(1)
        resultStep4 = self.items.getSearchResult(resultStep2[0])
        time.sleep(1)
        #print("Item name returned: " + SearchResult)
        # if selectItem != SearchResult:
        # print("Search result")
        self.ts.markFinal("test_searchItem", resultStep4, "Verify search result")
        self.driver.back()
