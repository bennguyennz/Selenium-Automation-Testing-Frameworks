import utilities.custom_logger as cl
import logging
from base.base_page import BasePage


class SearchItemPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _itemlist = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[1]/div[1]/div[2]/h5[1]/a[1]"
    #_itemSelect = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/h1[1]"
    _search_box = "search_query_top"
    _search_button = "submit_search"
    _search_result = "h5[itemprop='name'] a[class$='product-name']"


    ############################
    ### Element Interactions ###
    ############################

    # click category Women
    def clickCategory(self,category):
        if category == "Women":
            _category = "//a[@class='sf-with-ul'][normalize-space()='Women']"
        elif category == "Dresses":
            _category = "//div[@id='block_top_menu']/ul/li[2]/a[@title='Dresses']"
        elif category == "T-shirts":
            _category = "//div[@id='block_top_menu']/ul/li[3]/a[@title='T-shirts']"
        else:
            print("Category is not defined.")

        self.elementClick(locator=_category,locatorType="xpath")
        self.webScroll()
        self.webScroll()

    # Select an item and get its name
    def selectItem(self):
        SelectItem = self.getText(locator=self._itemlist,locatorType="xpath")
        #ItemList[1].click()
        #self.waitForElement(locator=self._itemSelect,locatorType="xpath")
        #SelectItem = self.getText(locator=self._itemSelect,locatorType="xpath")
        return SelectItem

    # Enter this item into page search box and begin search
    def searchItem(self,itemName):
        self.sendKeys(itemName,locator=self._search_box)
        self.elementClick(locator=self._search_button,locatorType="name")
        self.webScroll()

    # Verify search result
    def getSearchResult(self):
        SearchResult = self.getText(locator=self._search_result,locatorType="css")
        return SearchResult