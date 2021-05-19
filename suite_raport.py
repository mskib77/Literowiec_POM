import os
import unittest
from HtmlTestRunner import HTMLTestRunner
from tests.tests_on_main_activity import MainActivityTest


MA_tests = unittest.TestLoader().loadTestsFromTestCase(MainActivityTest)

# where test results should be written:
default_dir = os.getcwd()

# Creating the suit that contains all the tests:
test_suite = unittest.TestSuite([MA_tests])

# Uruchomenie suite:
if __name__ == "__main__":
    wyniki = f"{default_dir}/test_results"
    runner = HTMLTestRunner(output=wyniki, verbosity=2)
    runner.run(test_suite)