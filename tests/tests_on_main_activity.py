import unittest
from random import randint
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from ddt import ddt, data

from locators import MainActivityLocators
from tests.base_test import BaseTest
from tests.test_utils import TestUtils


@ddt
class MainActivityTest(BaseTest):

    def test_number_of_labels_is_correct(self):
        """ Passed if the number of scattered letters equals the length of the guessed word """
        ma = self.ma
        word = ma.get_nazwa_field().text  # the Word to build
        labels_list = ma.get_unordered_list_of_ids_of_shown_labels(MainActivityLocators.ALL_LABELS_IDS)
        num_of_letters = len(word)
        num_of_labels = len(labels_list)
        test_ok = num_of_labels == num_of_letters
        if not test_ok:
            TestUtils.screen_shot(self.driver, "Diffrent numbers of letters and labels")
        self.assertTrue(test_ok, f"Number of labels ({num_of_labels}) on the screen and number"
                                 f"of letters ({num_of_letters}) in the word differ. See screenshot. ")

    # @unittest.skip
    def test_from_lowercase_to_uppercase(self):
        ma = self.ma
        word_1 = ma.get_nazwa_field().text  # the Word to build in lowercase
        labels_id_list = ma.get_unordered_list_of_ids_of_shown_labels(MainActivityLocators.ALL_LABELS_IDS)
        labels_list_1 = []  # labels list in lowercase
        for idi in labels_id_list:
            labels_list_1.append(self.driver.find_element_by_id(idi))
        # "Rising" the word and labels:
        btn = self.ma.get_upper_lower_button()
        btn.click()
        # Checking after the 'rising':
        word_2 = ma.get_nazwa_field().text  # the Word to build in uppercase
        labels_id_list = ma.get_unordered_list_of_ids_of_shown_labels(MainActivityLocators.ALL_LABELS_IDS)
        labels_list_2 = []  # labels list in uppercase
        for idi in labels_id_list:
            labels_list_1.append(self.driver.find_element_by_id(idi))
        # Comparison:
        test_ok_1 = word_2 == word_1.upper()
        test_ok_2 = True
        for i in range(0, len(labels_list_2)):
            if labels_list_2[i].text != labels_list_1[i].text.upper():
                test_ok_2 = False
                break
        print(test_ok_1)
        print(test_ok_2)
        sleep(2)

    # causes the test to be run 'N' times
    # @data(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39)
    @data(1, 2, 3)  # causes the test to be run 'N' times
    # @unittest.skip
    def test_build_the_word(self, placeholder):
        """Wrapper for ddt.
         Real test is in __do_puzle() below
        """
        self.__do_puzzle()

    def __do_puzzle(self):
        """Passed if:
        1. There appears element WORD_BUILT containing the word we built manually from the labels/letters AND
        2. WORD_BUILT properly describes the picture AND
        3. There appears on the screen a big button with green arrow
        """
        ma = self.ma
        word = ma.get_nazwa_field().text  # the Word to build
        labels_list = ma.get_ordered_list_of_ids_of_shown_labels(word)

        # print("wykrylem etykiety na:")
        # for ids in labels_list:
        #     print(self.driver.find_element_by_id(ids).text, end=" ")
        # print("\n")

        # for i in range(labels_list):
        #     print(self.driver.find_element_by_id(labels_list[i]).text, end=" ")

        l_width, x0, yl, box_h = ma.get_dimensions(labels_list)
        rnd_range = int(box_h / 5)
        # Minor adjustments inspired by practice:
        x_curr = x0 + int(0.6 * l_width)
        l_width = int(0.95 * l_width)
        if len(labels_list) >= 12:
            l_width = int(0.85 * l_width)
        if len(labels_list) <= 6:
            x_curr = x0 + 3 * l_width
            l_width = int(1.2 * l_width)
        # end of adjustments

        for id_el in labels_list:
            ltd = self.driver.find_element_by_id(id_el)  # ltd - label to drag
            action = TouchAction(self.driver)
            rnd = randint(0, rnd_range)  # only for better visual effect ;)
            action.press(ltd).wait(300).move_to(x=x_curr, y=yl-rnd).perform().release()
            ltd.click()  # trick - only that REALLY releases touch on element
            sleep(0.5)
            x_curr += l_width

        # Testing conditions No 1:
        word_built = ma.get_word_built()

        # diagnostics - switch it off later:
        if word_built == -1:
            print("ułożono: ", word_built)
        else:
            print("zgadywano: ", word)
            print("ułożono:   ", word_built.text)

        test_ok_2 = True
        test_ok_3 = True

        test_ok_1 = (word_built != -1)

        # Testing conditions No 2:
        if test_ok_1:
            # The word we built can contain spaces, so:
            word_built_txt = word_built.text.replace(" ", "")
            test_ok_2 = (word_built_txt.upper() == word.upper())    # in case sbd clicks bUpper during test :(

            # Testing conditions No 3:
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
                        f"Error in test_build_the_word(self) Reason: {reasons} \nSee the picture: 'Error while doing the puzzle.png'")
