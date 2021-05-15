from time import sleep

from tests.base_test import BaseTest


class MainActivityTest(BaseTest):

    def test_dummy(self):
        sleep(1)
        pass

    def test_number_of_letters_is_correct(self):
        """Passed if number of scattered letters equals word length"""
        self.ma.long_touch_on_image()
        sleep(5)

    def test_daj_glos(self):
        sleep(2)
        self.ma.click_on_image()
        sleep(2)

    def test_podnies_upper(self):
        sleep(2)
        btn = self.ma.get_upper_lower_button()
        btn.click()
        sleep(1)
