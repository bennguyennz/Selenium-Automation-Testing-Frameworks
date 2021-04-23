import Utilities.custom_logger as cl
import logging
from Base.base_page import BasePage
import time

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
    _search_result = "//li[contains(@class,'ajax_block_product')]"
    #_search_result = "h5[itemprop='name'] a[class$='product-name']"


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
            _category = ""
            print("Category is not defined.")

        self.elementClick(locator=_category,locatorType="xpath")
        self.webScroll("down",800)

    # Select an item and get its name
    def selectItem(self,itemSearch):
        products = self.driver.find_elements_by_xpath("//li[contains(@class,'ajax_block_product')]")
        for product in products:
            elementproduct = product.find_element_by_xpath("div/div/h5/a").text
            if elementproduct == itemSearch:
                return elementproduct

    # Enter this item into page search box and begin search
    def searchItem(self,itemName):
        self.sendKeys(itemName,locator=self._search_box)
        self.elementClick(locator=self._search_button,locatorType="name")
        self.webScroll()

    # Verify search result
    def getSearchResult(self, SelectItem):
        #SearchResult = self.getText(locator=self._search_result,locatorType="css")
        products = self.driver.find_elements_by_xpath("//li[contains(@class,'ajax_block_product')]")
        #print(products)
        for product in products:
        #     if item.getElement(locator="div/div/h5/a",locatorType="xpath").text == SelectItem:
            elementproduct = product.find_element_by_xpath("div/div/h5/a")
            if elementproduct.text == SelectItem:
                time.sleep(1)
                elementproduct.click()
                self.webScroll()

        #return SearchResult