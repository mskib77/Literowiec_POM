import unittest
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from ddt import ddt, data
from selenium.common.exceptions import NoSuchElementException

from locators import MainActivityLocators
from tests.base_test import BaseTest
from tests.test_utils import TestUtils

@ddt
class MainActivityTest(BaseTest):

    @unittest.skip
    def test_number_of_letters_is_correct(self):
        """Passed if number of scattered letters equals word length"""
        self.ma.long_touch_on_image()
        sleep(5)

    @unittest.skip
    def test_daj_glos(self):
        sleep(2)
        self.ma.click_on_image()
        sleep(2)

    @unittest.skip
    def test_podnies_upper(self):
        sleep(2)
        btn = self.ma.get_upper_lower_button()
        btn.click()
        sleep(1)

    @unittest.skip
    def test_wypisuj_co_widzisz(self):
        sleep(1)
        ma = self.ma
        sleep(3)
        nazwa = ma.get_nazwa_field().text
        print(f"Pod obrazkiem widzę: {nazwa}")

        all_labels_list = MainActivityLocators.ALL_LABELS_IDS

        print(all_labels_list, len(all_labels_list))

        # speeding up
        self.driver.implicitly_wait(0.2)
        labels_shown = []
        for label in all_labels_list:
            try:
                found = self.driver.find_element_by_id(label)
                labels_shown.append(label)
            except NoSuchElementException:
                pass
        # restoring timeout:
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)
        print("labels_shown:")
        print(labels_shown, len(labels_shown))

    @unittest.skip
    # @data(1)
    def test_testuj(self, dummy):
        ma = self.ma
        word = ma.get_nazwa_field().text
        ma.get_ordered_list_of_shown_labels(word)
        sleep(1)

    def test_draging_first_letter(self):
        ma = self.ma
        word = ma.get_nazwa_field().text
        polozenie = ma.get_nazwa_field()
        l_list = ma.get_ordered_list_of_shown_labels(word)
        # label to drag:
        ltd = self.driver.find_element_by_id(l_list[0])

        action = TouchAction(self.driver);
        # action.long_press(ltd).wait(200).move_to(polozenie).perform().release() - to dziala!
        action.long_press(ltd).wait(200).move_to(x=200, y=200).perform().release()
        sleep(4)
        # action.longPress(elem1).waitAction(3000).moveTo(elem2).perform().release();
