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

    def __scroll_to(self, element):
        """Auxiliary: scrolling down till the @element appears"""
        MAX_SCROLLS_ALLOWED = 6    # to prevent infinite loop in case we can't find the @element
        x, y = TestUtils.get_screen_dimensions(self.driver)
        # speeding up a little:
        self.driver.implicitly_wait(2)
        # scrolling down till the INFO button appears:
        found = False
        scroll_number = 0
        while not found:
            try:
                el_we_seek = self.driver.find_element_by_id(element)
                found = True
            except NoSuchElementException:
                self.driver.swipe(x / 2, y * 0.9, x / 2, y * 0.1, 1000)
                scroll_number += 1
                if scroll_number > MAX_SCROLLS_ALLOWED:
                    raise NoSuchElementException(f"Cant't find element. Too many scrolls performed ({scroll_number}) "
                                                 f"while {MAX_SCROLLS_ALLOWED} allowed")
        # restoring timeout:
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)
        return el_we_seek

    def get_info_button(self):
        binfo = self.__scroll_to(SAL.BINFO_ID)
        return binfo

    def get_cb_nazwa(self):
        cb = self.__scroll_to(SAL.CB_NAZWA_ID)
        return cb

    def get_rb_nopicture(self):
        rb = self.__scroll_to(SAL.RB_NOPICTURE_ID)
        return rb
