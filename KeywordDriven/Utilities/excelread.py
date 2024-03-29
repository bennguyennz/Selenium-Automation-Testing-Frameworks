import xlrd
import Utilities.custom_logger as lg
from Utilities.Constants import Constants
import logging
#import sys

class excelUtil():

    log = lg.customLogger(logging.DEBUG)
    constants = Constants()

  # Open excel
    def setExcelFile(self,path):
        try:
            self.workbook = xlrd.open_workbook(path)
        except:
            self.log.error("Data file was not opened")

    # Get rowcount
    def getRowCount(self,sheetname):
        try:
            self.worksheet = ""
            self.worksheet = self.workbook.sheet_by_name(sheetname)
            iNum = self.worksheet.nrows+1
            return iNum
        except:
            self.log.error("Failed to get row count")

    # Get cell value
    def getCellData(self,RowNum,ColNum,sheetname):
        try:
            self.worksheet = ""
            self.worksheet = self.workbook.sheet_by_name(sheetname)
            self.CellData = str(self.worksheet.cell_value(RowNum,ColNum))
            return self.CellData
        except:
            self.log.error("Failed to get cell data: "+ str(RowNum)+ " "+ str(sheetname))

    # Search for a value and exit if found and return rowID
    def getRowContains(self,testname,ColNum,sheetname):
        RowNum = 0
        try:
            rowCount=0
            rowCount = self.getRowCount(sheetname)
            for RowNum in range(0,rowCount):
                if self.getCellData(RowNum,ColNum,sheetname) == testname:
                    break
        except:
            self.log.error("Row contains check failed")
        return RowNum

    # Return test steps count
    def getTestStepsCount(self,sheetname,testname,stepstart):
        try:
            rowCount=0
            rowCount = self.getRowCount(sheetname)
            i=0
            for i in range(stepstart,rowCount):
                if str(testname) != str(self.getCellData(i,self.constants.Col_TestCaseID,sheetname)):
                    return i
        except:
            self.log.error("Failed to get steps count")
            return 0

    # Return test steps count
    def getITCount(self,sheetn,testn,stepst):
        try:
            rowCount = 0
            rowCount = self.getRowCount(sheetn)
            i = 0
            for i in range(stepst, rowCount):
                if str(testn) != str(self.getCellData(i, self.constants.Col_TestCaseID, sheetn)):
                    return i
        except:
            self.log.error("Failed to get steps count")
            return 0

    # Return object xpath value
    def getLocator(self, sheetname, locatorKeyword):
        try:
            nTotalRow = self.getRowCount(sheetname)
            for nRow in range(0,nTotalRow):
                if locatorKeyword == "":
                    break
                elif str(locatorKeyword) == str(self.getCellData(nRow, 0, sheetname)):
                    locatorValue = str(self.getCellData(nRow, self.constants.Col_Locator, sheetname))
                    return locatorValue
        except:
            self.log.error("Failed to get object value")

    def getLocatorType(self, sheetname, locatorKeyword):
        try:
            nTotalRow = self.getRowCount(sheetname)
            for nRow in range(0, nTotalRow):
                if locatorKeyword == "":

                    break
                elif str(locatorKeyword) == str(self.getCellData(nRow, 0, sheetname)):
                    locatorType = str(self.getCellData(nRow, self.constants.Col_LocatorType, sheetname))
                    return locatorType
        except:
            self.log.error("Failed to get locator type")

    # Get test case iterations count
    def getTestIterations(self,sheetname,testname):
        try:
            isSheet = self.workbook.sheet_names()
            for i in range(len(isSheet)):
                if str(testname) == str(isSheet[i]):
                    iterate = 0
                    iterate = self.getITCount(sheetname,testname,1)
                else:
                    continue
            if iterate > 0:
                return iterate
            else:
                return 2
        except Exception as e:
            return 2


    # Get test data value if parametrized
    def getTestdatavalue(self,testname,data,rownum):
        try:
            self.test_work_sheet = self.workbook.sheet_by_name(testname)
            test_rows = self.test_work_sheet.nrows
            test_cols = self.test_work_sheet.ncols
            for irows in range(0,1):
                for icols in range(0,test_cols):
                    test_data_header = self.getCellData(irows,icols,testname)
                    if test_data_header == data:
                        testdata_value = self.getCellData(rownum, icols, testname)
                        return testdata_value
                    else:
                        pass
        except:
            pass



