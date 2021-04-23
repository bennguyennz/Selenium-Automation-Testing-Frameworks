import unittest
from Tests.home.login_tests import LoginTests
from Tests.item.checkout_item_tests import CheckOutItemTests
from Tests.item.search_item_tests import SearchItemTests


# Get all Tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CheckOutItemTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(SearchItemTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1,tc2,tc3])
unittest.TextTestRunner(verbosity=2).run(smokeTest)