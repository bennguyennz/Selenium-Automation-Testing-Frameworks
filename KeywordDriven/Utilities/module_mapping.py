from Driver.selenium_driver import SeleniumDriver

class driver_mapping(SeleniumDriver):

    def __init__(self,driver):
        super(driver_mapping, self).__init__(driver)
        self.driver = driver

    # Execute the keyword functions and return the status
    def execute_keyword(self,keyword,attribute,value,objectname):
        if keyword == 'navigate':
            result = None
            result = self.navigate(value)
            return result
        elif keyword == 'input':
            result = None
            result = self.sendKeys(value,objectname)
            return result
        elif keyword == "click":
            result = None
            result = self.elementClick(objectname)
            return result
        elif keyword == "wait":
            result = None
            result = self.wait(value)
            return result
        elif keyword == "select_checkbox":
            result = None
            result = self.select_checkbox(objectname,value)
            return result
        elif keyword == "select_dropdown":
            result = None
            result = self.select_dropdown(objectname,value)
            return result
        elif keyword == "unselect_checkbox":
            result = None
            result = self.unselect_checkbox(objectname,value)
            return result
        elif keyword == "select_radio":
            result = None
            result = self.select_radio(objectname,value)
            return result
        elif keyword == "scroll":
            result = None
            result = self.webScroll(value)
            return result
        elif keyword == "verify":
            result = None
            result = self.verify(attribute,value,objectname)
            return result
        elif keyword == "moveto":
            result = None
            result = self.moveto(objectname)
            return result
        elif keyword == "waitfor":
            element_wait = self.waitforelement(value)
            if element_wait:
                return True
            elif element_wait is None:
                return False
            else:
                return False
        elif keyword == 'snapshot':
            result = None
            result = self.capturescreen()
            return result
        elif keyword == "dragto":
            result = None
            result = self.dragndrop(objectname,value)
            return result
        elif keyword == "closebrowser":
            result = None
            result = self.closebrowser()
            return result
        elif keyword == "switchto":
            result = None
            result = self.switchto(attribute,value)
            return result
        elif keyword == "waitfor":
            result=None
            result=self.waitforelement(objectname)
            return result
        elif keyword == "savedata":
            result=None
            result = self.savedata(objectname,value)
            return result
        elif keyword == "dbconnect":
            result=None
            result=self.dbconnect()
            return result
        elif keyword == "draftquery":
            result = None
            result = self.draftquery(value)
            return result
        elif keyword == "concat":
            result = None
            result = self.concat(value)
            return result
        elif keyword == "executequery":
            result = None
            result = self.executequery()
            return result
        elif keyword == "getdbvalue":
            result = None
            result = self.getdbvalue(value)
            return result
        elif keyword == "compare":
            result = None
            result = self.compare()
            return result
        elif keyword == "doubleclick":
             result = None
             result = self.doubleClick(objectname)
             return result
        else:
            self.log.info("Bad keyword or not found. All keywords should be in lowercase!!")
            return False


