import unittest
from tests.home.logintests import LoginTests
#import utilities.HTMLTestRunner
#from tests.items.checkout_item_tests import RegisterCoursesCSVDataTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
#tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

# Create a test suite combining all test classes
#smokeTest = unittest.TestSuite([tc1, tc2])
smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)