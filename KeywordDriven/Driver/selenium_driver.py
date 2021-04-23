from selenium.webdriver.common.by import By
######### For Explicit wait import below
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import Utilities.custom_logger as lg
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from Utilities.Constants import Constants
#import cx_Oracle
import re
##################################################
import time
import logging

class SeleniumDriver():


    # Create object instance for logging
    log = lg.customLogger(logging.DEBUG)

    # Set init value for driver and Constants
    def __init__(self,driver):
        self.driver = driver
        self.constants = Constants()
        self.UIvalue = None
        self.DBvalue = None
        self.finalquery = None
        self.rawquery = None


    # Method for browser navigation
    def navigate(self,datavalue):
        try:
            self.driver.get(datavalue)
            return True
        except:
            self.log.error("Navigation failed")
            return False

    # Get web element based on the locator value
    def getelement(self,locator):
        try:
            element = self.driver.find_element(By.XPATH,locator)
        except:
            self.log.info("Element not found")

        return element


    # Method to find web element occurance
    def findelement(self,locator):
        try:

            elementtofind = None
            elementtofind = self.driver.find_elements(By.XPATH,locator)
            # If element occurance found then return True
            if len(elementtofind) > 0:
                return True
            else:
                return False
                self.log.info("Element not found")
        except:
            self.log.info("Some error occured, element not found")
            return False

    # Method to wait for an element
    def waitforelement(self,locator):
        try:
            elementowait = None
            nwait=None
            # wait object with certain seconds and ignoring conditions
            nwait = WebDriverWait(self.driver,10,poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,
                                                     ElementNotSelectableException])
            # Wait for an element until the expected conditions are met
            elementowait = nwait.until(EC.presence_of_element_located((By.XPATH,locator)))
            return elementowait

        except Exception as e:
            self.log.info("Element was not found, wait limit exceeded: "+str(e.args))
            return False



    # Method to perform element click
    def elementClick(self,locator):
        try:
            self.getelement(locator).click()
            return True
        except:
            self.log.info("Element not clicked")
            return False

    # Method to enter/type text
    def sendKeys(self,data,locator):
        try:
            self.getelement(locator).clear()
            self.getelement(locator).send_keys(data)
            return True
        except:
            self.log.info("Cannot send data to the element")
            return False

    # Method to capture screenshot
    def capturescreen(self):

        try:
            filename = "Scrnshot"+"_"+str(round(time.time()*1000))+".png"
            folder_location = self.constants.Path_Snapshot
            destination = folder_location+filename
            self.driver.save_screenshot(destination)
            return True
        except NotADirectoryError:
            self.log.info("Capture screenshot failed")
            return False

    # Method to get page title
    def getTitle(self):
        return self.driver.title

    # Method for scrolling of web page
    def webScroll(self,direction):

        try:
            if direction == 'up':
                self.driver.execute_script("window.scrollBy(0,-400);")
                return True
            elif direction == 'down':
                self.driver.execute_script("window.scrollBy(0,400);")
                return True
            elif direction == 'up2x':
                self.driver.execute_script("window.scrollBy(0,-800);")
                return True
            elif direction == 'down2x':
                self.driver.execute_script("window.scrollBy(0,800);")
                return True
            elif direction == 'right':
                self.driver.execute_script("window.scrollBy(1000,0);")
                return True
            else:
                self.driver.execute_script("window.scrollBy(-1000,0);")
                return True
        except:
            self.log.error("Scrolling failed")
            return False


    # Method to Select value from the dropdown
    def select_dropdown(self,locator,value):
        try:
            dropdownlist = Select(self.driver.find_element(By.XPATH, locator))
            dropdownlist.select_by_visible_text(value)

            # drop_down = self.driver.find_element(By.ID, locator)
            # sel_element = Select(drop_down)
            # sel_element.select_by_value(value)
            return True
        except:
            self.log.error("Dropdown selection failed")
            return False

    # Method to Select radio button
    def select_radio(self,locator,datavalue):
        try:
            #update locator xpath with parameter datavalue
            ulocator = locator.format(datavalue)
            nradio = self.driver.find_element(By.XPATH,ulocator)
            nradio.click()
            ulocator = ""
            return True
        except:
            self.log.error("Select radio button failed")
            return False

    # Method to Select checkbox
    def select_checkbox(self,locator,datavalue):

        try:
            #update locator xpath with parameter datavalue
            ulocator = locator.format(datavalue)
            ncheckbox = self.driver.find_element(By.XPATH,ulocator)
            isSelected = ncheckbox.is_selected()
            if not isSelected:
                ncheckbox.click()
                ulocator = ""
                return True
        except:
            self.log.error("Select checkbox failed")
            return False


    # Method to unselect checkbox
    def unselect_checkbox(self,locator,datavalue):

        try:
            #update locator xpath with parameter datavalue
            ulocator = locator.format(datavalue)
            ncheckbox = self.driver.find_element(By.XPATH,ulocator)
            isSelected = ncheckbox.is_selected()
            if isSelected:
                ncheckbox.click()
                ulocator = ""
                return True
        except:
            self.log.error("Unselect of checkbox failed")
            return False

    # Method to wait
    def wait(self,datavalue):
        try:
            nseconds = int(float(datavalue))
            time.sleep(nseconds)
            return True
        except:
            self.log.error("Wait for failed")
            return False

    # Method to verify Text, enabled, selected, displayed, exists, title
    def verify(self,property,value,locator):
        try:
            if property == "text":
                UI_Text = None
                UI_Text = self.driver.find_element(By.XPATH,locator).text
                if str(UI_Text) == str(value):
                    return True
                else:
                    return False
            elif property == "enabled":
                enable_flag = None
                enable_flag = self.driver.find_element(By.XPATH,locator).is_enabled()
                if str(enable_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "selected":
                select_flag = None
                select_flag = self.driver.find_element(By.XPATH, locator).is_selected()
                if str(select_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "displayed":
                display_flag = None
                display_flag = self.driver.find_element(By.XPATH, locator).is_displayed()
                if str(display_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "exists":
                exist_flag = None
                exist_flag = self.findelement(locator)
                if str(exist_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "title":
                title = str(self.getTitle())
                if title == value:
                    return True
                else:
                    return False

        except:
            self.log.error("Verify failed")
            return False

    # Method to move cursor to an element
    def moveto(self,locator):
        try:
            element = None
            element = self.driver.find_element(By.XPATH,locator)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            return True
        except:
            self.log.error("Cursor Move to element failed")
            return False

    # Method to drag and drop element from source to destination
    def dragndrop(self,locator,value):
        try:
            from_element = self.driver.find_element(By.XPATH,locator)
            to_element = self.driver.find_element(By.XPATH,value)
            action = ActionChains(self.driver)
            action.drag_and_drop(from_element,to_element).perform()
            return True
        except:
            self.log.error("Drag and drop failed")
            return False


    # Method to close browser
    def closebrowser(self):
        try:
            self.driver.close()
            return True
        except:
            self.log.error("Close browser failed")
            return False


    def switchto(self,property,value):
        try:
            if not value.isalpha():
                value = int(float(value))
                value = value - 1
            else:
                value = str(value)

            if property == "window":
                current_window = self.driver.window_handles[value]
                self.driver.switch_to.window(current_window)
                return True
            elif property == "frame":
                if value == "default":
                    self.driver.switch_to.default_content()
                    return True
                else:
                    self.driver.switch_to.frame(value)
                    return True
            elif property == "alert":
                alertpop = self.driver.switch_to.alert
                if value == "accept":
                    alertpop.accept()
                    return True
                elif value == "dismiss":
                    alertpop.dismiss()
                    return True
                else:
                    alert_text = str(alertpop.text)
                    if  value in alert_text:
                        return True
                    else:
                        return False
        except:
            self.log.error("Failed to switch to: "+str(property))
            return False



    # Get UI value in a variable
    def savedata(self,locator,value):
        try:
            value = None
            value = str(self.driver.find_element(By.XPATH,locator).text).strip()
            self.UIvalue = value
            #print("UI value is "+self.UIvalue)
            return True
        except:
            self.log.error("Failed to get data value from UI")
            return False


    # Connect to DB via oracle string
    # def dbconnect(self):
    #     try:
    #         self.conn = cx_Oracle.Connection(self.constants.Conn_String)
    #         # link cursor to the connection
    #         self.curr = self.conn.cursor()
    #         return True
    #     except:
    #         self.log.error("DB connection failed")
    #         return False


    # Get draft query
    def draftquery(self,value):
        try:
            self.rawquery = str(value)
            #print("query is "+str(value))
            return True
        except:
            self.log.error("Failed to get draft query")
            return False

    # Concat draft query
    def concat(self,value):
        try:
            self.finalquery = self.rawquery + " " + str(value)
            self.rawquery = self.finalquery
            return True
        except:
            self.log.error("Failed to concat query")
            return False

    # Execute the query
    def executequery(self):
        try:
            if self.finalquery is None:
                self.resultset = self.curr.execute(self.rawquery)
            else:
                self.resultset = self.curr.execute(self.finalquery)
            return True
        except:
            self.log.error("Execute query failed")
            return False

    # Get db value
    def getdbvalue(self,value):
        try:
            value = None
            self.result_list = self.resultset.fetchall()

            for rows in self.result_list:
                value = str(rows[0])
                self.DBvalue = value
                #print("DB value "+self.DBvalue)
            self.curr.close()
            self.conn.close()
            return True

        except:
            self.log.error("Failed to get db value into a variable")
            return False


    # compare db and UI value
    ###########
    # def compare(self):
    #     try:
    #         # Using regex match only alphanumeric characters excluding special characters
    #         # and replacing with blank character
    #         nDBvalue = re.sub("[^\w\.]", "", self.DBvalue)
    #         nUIvalue = re.sub("[^\w\.]", "", self.UIvalue)
    #         # compare db and UI value
    #         if nDBvalue == nUIvalue:
    #             return True
    #         else:
    #             return False
    #     except:
    #         self.log.error("Comparison between DB and UI value failed")
    #         return False
#############B

            # Method to perform element click

    def doubleClick(self, locator):
        try:
            element = None
            element = self.getelement(locator)
            action = ActionChains(self.driver)
            action.double_click(element).perform()
            return True
        except:
            self.log.error("Double Click on the element failed")
            return False









































