from selenium.common.exceptions import NoSuchElementException
from locators import SettingsActivityLocators as SAL
from tests.test_utils import TestUtils


class SettingsActivity:

    def __init__(self, sterownik):
        self.driver = sterownik

    def _get_checkable_elements_list(self):
        try:
            list_of_elems = self.driver.find_elements_by_android_uiautomator('new UiSelector().checkable(true)')
        except NoSuchElementException:
            list_of_elems = []
        return list_of_elems

    def settings_elements_present(self):
        checkable_list = self._get_checkable_elements_list()
        return checkable_list is not []

    def _scroll_to(self, element):
        """Auxiliary: scrolling down till the @element button appears"""

        x, y = TestUtils.get_screen_dimensions(self.driver)
        # speeding up a little:
        self.driver.implicitly_wait(1)
        # scrolling down till the INFO button appears:
        found = False
        while not found:
            print("WCHODZE*****************")

            try:
                self.driver.find_element_by_id(element)
                found = True
            except NoSuchElementException:
                self.driver.swipe(x / 2, y * 0.9, x / 2, y * 0.1, 1000)
        # restoring timeout:
        print("wychodze....................................")
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)

    # def _scroll_to_info_button(self):
    #     """Auxiliary: scrolling down till the INFO button appears"""
    #
    #     x, y = TestUtils.get_screen_dimensions(self.driver)
    #     # speeding up a little:
    #     self.driver.implicitly_wait(1)
    #     # scrolling down till the INFO button appears:
    #     found = False
    #     while not found:
    #         try:
    #             self.driver.find_element(*SAL.BINFO)
    #             found = True
    #         except NoSuchElementException:
    #             self.driver.swipe(x / 2, y * 0.9, x / 2, y * 0.1, 1000)
    #     # restoring timeout:
    #     self.driver.implicitly_wait(TestUtils.WAIT_TIME)

    def get_info_button(self):
        self._scroll_to(SAL.BINFO_id)
        binfo = self.driver.find_element(*SAL.BINFO)
        return binfo

    def get_cb_nazwa(self):
        self._scroll_to(SAL.CB_NAZWA_id)
        cb = self.driver.find_element(*SAL.CB_NAZWA)
        return cb

    def get_rb_nopicture(self):
        self._scroll_to(SAL.RB_NOPICTURE_id)
        rb = self.driver.find_element(*SAL.RB_NOPICTURE)
        return rb
