import unittest
from tests.home.logintests import LoginTests
from tests.items.checkout_item_tests import CheckOutItemTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CheckOutItemTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1],[tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)