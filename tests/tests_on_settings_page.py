from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.base_test import BaseTest
from tests.test_utils import TestUtils
from locators import SettingsActivityLocators as SAL
from locators import MainActivityLocators as MAL
from locators import InfoActivityLocators as IAL


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

    def test_switching_off_word_and_picture(self):
        """ Is switching off the picture and the word (nazwa) under the picture effective?
        Passed if:
        1. Picture is not visible AND
        2. Word under the picture is not visible
        """
        sa = self.sa
        ma = self.ma
        cb_nazwa = sa.get_cb_nazwa()
        cb_nazwa.click()
        rb_nopicture = sa.get_rb_nopicture()
        rb_nopicture.click()
        # Going back to Main Activity:
        self.driver.back()
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.OBSZAR))

        # speeding up a little:
        self.driver.implicitly_wait(2)

        try:
            ma.get_image()
            test_image_ok = False
        except NoSuchElementException:
            test_image_ok = True

        try:
            ma.get_nazwa_field()
            test_nazwa_ok = False
        except NoSuchElementException:
            test_nazwa_ok = True

        # restoring timeout (just in case... ;)
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)

        test_ok = test_image_ok and test_nazwa_ok

        self.assertTrue(test_ok, "Image and/or word underneath still present despite switching them off!")

    # @unittest.skip
    def test_switching_to_info_activity(self):
        """
        Can switch to Info?
        Passed if:
        1. there is "android:id/action_bar_title element in the activity we switch to AND
        2. it contains "Informacje o aplikacji" text
        """
        sa = self.sa
        ia = self.ia
        binfo = sa.get_info_button()
        binfo.click()
        test_ok = False
        try:
            WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(IAL.ACTION_BAR_TITLE))
            el = ia.get_action_bar_title()
            if el.text.upper() == "Informacje o aplikacji".upper():
                test_ok = True
        except TimeoutException:
            test_ok = False
        finally:
            sleep(2)

        self.assertTrue(test_ok, "Info activity did not appear!")




