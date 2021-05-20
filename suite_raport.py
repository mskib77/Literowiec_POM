import os
import unittest
from HtmlTestRunner import HTMLTestRunner
from tests.tests_on_main_activity import MainActivityTest
from tests.tests_on_settings_page import SettingsPageTest


MA_tests = unittest.TestLoader().loadTestsFromTestCase(MainActivityTest)
SA_tests = unittest.TestLoader().loadTestsFromTestCase(SettingsPageTest)

# where test results should be written:
default_dir = os.getcwd()

# Creating the suit that contains all the tests:
test_suite = unittest.TestSuite([MA_tests, SA_tests])

# Uruchomenie suite:
if __name__ == "__main__":
    wyniki = f"{default_dir}/test_results"
    runner = HTMLTestRunner(output=wyniki, verbosity=2)
    runner.run(test_suite)