from Utilities.Test_Status import TrackStatus
import unittest
import pytest
#rom ddt import ddt, data, unpack
from Utilities.Constants import Constants
from Utilities.excelread import excelUtil
from Utilities.keyword_mapping import driver_mapping
import Utilities.custom_logger as lg
import logging

@pytest.mark.usefixtures("invoke_browser")
#@ddt
class mainTests(unittest.TestCase):

    log = lg.customLogger(logging.INFO)

    # Initialize object instances for test case result, constants, exceldata, method mapping
    @pytest.fixture(autouse=True)
    def initialSetup(self,invoke_browser):
        self.ts = TrackStatus(self.driver)
        self.constants = Constants()
        self.excel = excelUtil()
        self.drivermethod = driver_mapping(self.driver)

    # This is the main method that kicks in when execution starts (This in turn calls all the keywords)
    @pytest.mark.run(order=1)
    def test_main(self):
        self.excel.setExcelFile(self.constants.Path_TestData)
        self.execute_testCases()


    # Reads keywords, objects and other attributes to execute methods
    def execute_testCases(self):
        # Get row count in test suite worksheet
        ntotalTestCases = self.excel.getRowCount(self.constants.Sheet_TestSuite)

        # loop through testsuite
        # worksheet and get test ids (Row id 1 thru last row)
        for ntestCase in range(1,(ntotalTestCases-1)):
            # Get test case id from test suite worksheet
            nTestCaseID = self.excel.getCellData(ntestCase, self.constants.Col_TestCaseID, self.constants.Sheet_TestSuite)
            # Get test case description
            nTestCaseDescription = self.excel.getCellData(ntestCase, self.constants.Col_TestCaseDescription, self.constants.Sheet_TestSuite)
            # Get runmode from testsuite worksheet
            sRunMode = self.excel.getCellData(ntestCase, self.constants.Col_RunMode, self.constants.Sheet_TestSuite)

            # If runmode is Yes then get first and last position of testcase id in TestSteps worksheet
            if sRunMode == 'Yes':
                testsheet_name = nTestCaseID
                test_iterations = self.excel.getTestIterations(nTestCaseID, testsheet_name)
                self.log.info("Number of test iterations: "+str(test_iterations-1))
                # Get number of iterations for a test case id (Sheetname will be test case id)
                # If no entries in test data sheet then execute for loop only once
                # Start for loop with number of entries
                self.log.info("*****************************************************************************************************")
                self.log.info("Test case: " + str(nTestCaseID) + ":" + str(nTestCaseDescription))
                self.log.info("*****************************************************************************************************")
                # Start id of test step based on the tc id
                for ntest in range(1, test_iterations):
                    nStartStep = self.excel.getRowContains(nTestCaseID,self.constants.Col_TestCaseID,self.constants.Sheet_TestSteps)
                    # Last id of test step based on the tc id
                    nEndStep = self.excel.getTestStepsCount(self.constants.Sheet_TestSteps,nTestCaseID,nStartStep)
                    # Traverse through test steps
                    for step in range(nStartStep,nEndStep):
                            # Get test step id
                            ntestStepId = self.excel.getCellData(step,self.constants.Col_TestScenarioID,self.constants.Sheet_TestSteps)
                            # Get step description
                            nstepDescription = self.excel.getCellData(step,self.constants.Col_TestDescription,self.constants.Sheet_TestSteps)
                            # Get object name
                            nLocatorKeyword = self.excel.getCellData(step, self.constants.Col_LocatorKeyword, self.constants.Sheet_TestSteps)
                            # Get object xpath value
                            nLocator = self.excel.getLocator(self.constants.Sheet_Locators, nLocatorKeyword)
                            nLocator_Type = self.excel.getLocatorType(self.constants.Sheet_Locators, nLocatorKeyword)
                            # Get action keyword
                            nActionKeyword = self.excel.getCellData(step, self.constants.Col_ActionKeyword,self.constants.Sheet_TestSteps)
                            # Get property value
                            nPageProperty = self.excel.getCellData(step, self.constants.Col_PageProperty, self.constants.Sheet_TestSteps)
                            # Get data value (for dragto keyword datavalue should have xpath value)
                            if nActionKeyword == "dragto" or nActionKeyword == "waitfor":
                                tempdata = self.excel.getCellData(step, self.constants.Col_TestData, self.constants.Sheet_TestSteps)
                                ndataValue = self.excel.getLocator(self.constants.Sheet_Locators, tempdata)
                            else:
                                ndataValue = self.excel.getCellData(step, self.constants.Col_TestData, self.constants.Sheet_TestSteps)
                            testdata_value = self.excel.getTestdatavalue(nTestCaseID,ndataValue,ntest)
                            if testdata_value is None:
                                testdata_value = ndataValue
                            else:
                                testdata_value = testdata_value

                            #**********************************************
                            # Get data value from test data spreadsheet
                            #**********************************************
                            # store step execution status (Pass/Fail)
                            stepresult = self.drivermethod.execute_keyword(nActionKeyword,nPageProperty,testdata_value,nLocator,nLocator_Type)
                            self.ts.mark(stepresult,nstepDescription)
                    # Test case status (Pass or Fail)
                    self.ts.markFinal(nTestCaseID,stepresult,nTestCaseDescription)












