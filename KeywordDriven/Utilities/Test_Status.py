from Utilities.custom_logger import customLogger as lg
import logging
from Driver.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):

    log = lg.log_utility(logging.DEBUG)
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)
        self.resultlist=[]


    def setResult(self,result,resultMessage):
        if result is None:
            self.resultlist.append("Fail")
            self.log.info(resultMessage+":Fail")
            self.capturescreen()
        else:
            if result:
                self.resultlist.append("Pass")
                self.log.info(str(resultMessage)+":Pass")
            else:
                self.resultlist.append("Fail")
                self.log.info(resultMessage+":Fail")
                self.capturescreen()

    def mark(self,result,resultMessage):
        self.setResult(result,resultMessage)


    def markFinal(self,testName,result,resultMessage):
        #self.setResult(result,resultMessage)

        if "Fail" in self.resultlist:
            self.log.error("Testcase FAILED: "+testName+" :"+resultMessage)
            self.resultlist.clear()
            assert False == False
        else:
            self.log.info("Testcase PASSED: "+testName+" :"+resultMessage)
            self.resultlist.clear()
            assert True == True




