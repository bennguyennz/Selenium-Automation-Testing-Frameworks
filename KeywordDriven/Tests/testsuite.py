import unittest
from Tests.main_tests import mainTests


tc1 = unittest.TestLoader().loadTestsFromTestCase(mainTests)

smokeTest = unittest.TestSuite([tc1])
unittest.TextTestRunner(verbosity=2).run(smokeTest)