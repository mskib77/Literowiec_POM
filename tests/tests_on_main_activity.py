import unittest
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from tests.base_test import BaseTest
from tests.test_utils import TestUtils


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

    def test_wypisuj_co_widzisz(self):
        ma = self.ma
        nazwa = ma.get_nazwa_field().text
        print(f"Pod obrazkiem widzę: {nazwa}")

        all_labels_list = TestUtils.prepare_list_of_all_labels_ids()

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
