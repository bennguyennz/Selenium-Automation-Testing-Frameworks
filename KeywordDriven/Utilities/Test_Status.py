import Utilities.custom_logger as cl
import logging
from Driver.selenium_driver import SeleniumDriver
from traceback import print_stack


class TrackStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TrackStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("## VERIFICATION SUCCESSFUL: " + resultMessage + " ####")
                else:
                    self.resultList.append("FAIL")
                    self.log.error("## VERIFICATION FAILED: " + resultMessage + " ####")
                    self.capturescreen(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("## VERIFICATION FAILED: " + resultMessage + " ####")
                self.capturescreen(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("## Exception Occurred!!!" + " ####")
            self.capturescreen(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):

        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + " ***** TEST FAILED" + " *****")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ###### TEST SUCCESSFUL" + " #####")
            self.resultList.clear()
            assert True == True
