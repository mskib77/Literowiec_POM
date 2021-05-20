from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.base_test import BaseTest
from tests.test_utils import TestUtils
from locators import SettingsActivityLocators as SAL
from locators import MainActivityLocators as MAL


class SettingsPageTest(BaseTest):

    def setUp(self):
        """Going to Settings Activity before each test"""
        super().setUp()
        self._go_to_settings_page(self.driver)

    def _go_to_settings_page(self, driver):
        """ Auxiliary; brings up the Settings activity. Starts from MainActivity """
        """ Called by setUp() """
        self.ma.long_touch_on_image()
        WebDriverWait(driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(SAL.TITLE))

    def test_dummy(self):
        pass

    def test_switching_off_word_and_picture(self):
        """ Is switching off the picture and the word under the picture effective? """
        sa = self.sa
        cb_nazwa = sa.get_cb_nazwa()
        cb_nazwa.click()
        rb_nopicture = sa.get_rb_nopicture()
        rb_nopicture.click()
        # Going to Main Activity:
        self.driver.back()
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.OBSZAR))
        sleep(5)



