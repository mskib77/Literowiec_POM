import unittest
from random import randint
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from ddt import ddt, data
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
    def test_podnies_upper(self):
        sleep(2)
        btn = self.ma.get_upper_lower_button()
        btn.click()
        sleep(1)

    @unittest.skip
    def test_test_draguj2(self):
        ma = self.ma
        word = ma.get_nazwa_field().text
        l_list = ma.get_ordered_list_of_ids_of_shown_labels(word)
        # element to drag:
        ltd = self.driver.find_element_by_id(l_list[0])
        action = TouchAction(self.driver)
        action.long_press(ltd).wait(200).move_to(x=100, y=740).perform().release()
        sleep(1)
        ltd = self.driver.find_element_by_id(l_list[1])
        action = TouchAction(self.driver)
        action.long_press(ltd).wait(200).move_to(x=150, y=740).perform().release()
        sleep(1)

    @data(1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1)
    def test_build_the_word(self, dummy):
        """Passed if:
        1. There appears element WORD_BUILT containing the word we built manually from the labbels/letters AND
        2. WORD_BUILT properly describes the picture AND
        3. There appears on the screen a big button with green arrow
        """

        ma = self.ma
        word = ma.get_nazwa_field().text
        labels_list = ma.get_ordered_list_of_ids_of_shown_labels(word)
        x_curr = -20
        y0 = 740
        l_width_set = False     # label width
        for id_el in labels_list:
            # ltd - label to drag:
            ltd = self.driver.find_element_by_id(id_el)

            if not l_width_set:
                l_Obszar = self.driver.find_element_by_id('autyzmsoft.pl.literowiec:id/l_Obszar')
                lokacja = l_Obszar.location
                wymiary = l_Obszar.size
                print("l_Obszar lokacja:", lokacja)
                print("l_Obszar wymiary", wymiary)


                sizes = ltd.size
                dx: int = sizes.get('width')
                print(f"x={dx}")
                l_width_set = True

            action = TouchAction(self.driver)
            x_curr += dx - dx/5
            action.press(ltd).wait(200).move_to(x=x_curr, y=y0+randint(0,100)).perform().release()
            ltd.click()  # trick - REALLY releases touch on element
            sleep(0.2)
        # Testing conditions No 1:
        word_built = ma.get_word_built()

        if word_built == -1:
            print("ułożono: ", word_built)
        else:
            print("zgadywano: ", word)
            print("ułożono:   ", word_built.text)

        test_ok_2 = True
        test_ok_3 = True

        test_ok_1 = (word_built != -1)

        if test_ok_1:
            # The word we built can contain spaces, so:
            word_built_txt = word_built.text.replace(" ", "")
            test_ok_2 = (word_built_txt == word)

            if test_ok_2:
                b_dalej = ma.get_bdalej_button()
                test_ok_3 = (b_dalej != -1)

        test_ok = test_ok_1 and test_ok_2 and test_ok_3

        if not test_ok:
            TestUtils.screen_shot(self.driver, "Error while doing the puzzle")

        # Determining the reason(s) of negative test:
        reasons = []
        if not test_ok_1: reasons.append("The word we have built does not appear")
        if not test_ok_2: reasons.append("The word we have build does not describe the picture")
        if not test_ok_3: reasons.append("The button with green arrow did not appear")

        self.assertTrue(test_ok,
                        f"Error in test_build_the_word(self) Reason: {reasons} \nSee picture 'Error while doing the puzzle.png'")
