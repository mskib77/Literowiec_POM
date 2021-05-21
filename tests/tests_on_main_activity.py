import unittest
from random import randint
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from ddt import ddt, data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainActivityLocators as MAL
from locators import SettingsActivityLocators as SAL
from tests.base_test import BaseTest
from tests.test_utils import TestUtils


@ddt
class MainActivityTest(BaseTest):

    # No 1 test case in documentation
    # @data(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39)
    @data(1, 2, 3, 4)  # causes the test to be run 'N' times
    # @unittest.skip
    def test_build_the_word(self, placeholder):
        """Passed if:
         1. There appears element WORD_BUILT containing the word we built manually from the labels/letters AND
         2. WORD_BUILT properly describes the picture AND
         3. There appears on the screen a big button with green arrow
         """
        ma = self.ma
        # every second puzzle should be done while in uppercase, so 'uppcasing' the word and labels:
        if placeholder % 2 == 0:
            btn = ma.get_upper_lower_button()
            sleep(1)  # for better visual effect
            btn.click()

        word = ma.get_nazwa_field().text  # the Word to build
        labels_list = ma.get_ordered_list_of_ids_of_shown_labels(word)
        # getting some physical dimensions needed to start doing puzzle:
        l_width, x_curr, yl, box_h = ma.get_dimensions(labels_list)
        rnd_range = int(box_h / 5)  # modifying 'dropping' place - only for visual effect ;)

        # Actual physical action - doing the puzzle:
        self.__move_Labels_to_places(labels_list, x_curr, l_width, yl, rnd_range)

        # Testing conditions No 1:
        word_built = ma.get_word_built()

        # diagnostics - switch it off later:
        if word_built == -1:
            print("ułożono: ", word_built)
        else:
            print("zgadywano: ", word)
            print("ułożono:   ", word_built.text)

        test_ok_1 = (word_built != -1)

        test_ok_2 = True
        test_ok_3 = True

        # Testing conditions No 2:
        if test_ok_1:
            # The word we built can contain spaces, so:
            word_built_txt = word_built.text.replace(" ", "")
            test_ok_2 = (word_built_txt == word)

            # Testing conditions No 3:
            if test_ok_2:
                b_dalej = ma.get_bdalej_button()
                test_ok_3 = (b_dalej != -1)

        test_ok = test_ok_1 and test_ok_2 and test_ok_3

        if not test_ok:
            TestUtils.screen_shot(self.driver, "Error while doing the puzzle")

        # Determining the reason(s) of negative test (if any):
        reasons = []
        if not test_ok_1: reasons.append("The word we have built does not appear")
        if not test_ok_2: reasons.append("The word we have built does not describe the picture")
        if not test_ok_3: reasons.append("The button with green arrow did not appear")

        self.assertTrue(test_ok,
                        f"Error in test_build_the_word(self) Reason: {reasons} \nSee the picture: 'Error while doing the puzzle.png'")

    # No 2 test case in documentation
    def test_build_the_word_incorrectly(self):
        """ What happens after we've built the word incorrectly. """
        """Passed if:
         1. All labels are placed in the red box in such a way that they do not form the proper word AND
         2. The big button with green arrow do NOT appear
         """
        ma = self.ma
        word = ma.get_nazwa_field().text  # the Word to build
        labels_list = ma.get_ordered_list_of_ids_of_shown_labels(word)
        # getting some physical dimensions needed to start doing puzzle:
        l_width, x_curr, yl, box_h = self.ma.get_dimensions(labels_list)

        # Meeting cond. No 1 - DELIBERATELY mixing labels_list in order not to built the proper word:
        labels_list[-1], labels_list[-2] = labels_list[-2], labels_list[-1]
        # Actual physical action - doing the puzzle:
        self.__move_Labels_to_places(labels_list, x_curr, l_width, yl, 0)

        b_dalej = ma.get_bdalej_button()
        test_ok = (b_dalej == -1)  # if not found - that's ok

        if not test_ok:
            TestUtils.screen_shot(self.driver, "Green button present after improperly doing the puzzle")

        self.assertTrue(test_ok, "Green button present after improperly doing the puzzle! See screenshot.")

    # No 3 test case in documentation
    def test_clicking_At_button(self):
        """ What happens after we click @ button?
        Passed if:
        1. The word under the picture does not change AND
        2. Labels scattered on the screen do change their positions AND
        3. Labels contain the same set of letters as before
        """
        ma = self.ma
        word_1 = ma.get_nazwa_field().text
        list_1 = ma.get_unordered_list_of_ids_of_shown_labels(MAL.ALL_LABELS_IDS)
        placeholder, letters_on_labels_1 = self.__get_word_and_labels_list()
        # Shifting to uppercase:
        b_again = ma.get_bagain_button()
        b_again.click()
        #
        word_2 = ma.get_nazwa_field().text
        list_2 = ma.get_unordered_list_of_ids_of_shown_labels(MAL.ALL_LABELS_IDS)
        # Testing conditions 1, 2, 3:
        test_ok_1 = (word_2 == word_1)
        test_ok_2 = (list_1 != list_2)
        placeholder, letters_on_labels_2 = self.__get_word_and_labels_list()
        a = set(letters_on_labels_1)
        b = set(letters_on_labels_2)
        test_ok_3 = (a == b)

        # Determining the reason(s) of negative test (if any):
        reasons = []
        if not test_ok_1: reasons.append("Words under the picture differ!")
        if not test_ok_2: reasons.append("Labels on screen did not chane their positions!")
        if not test_ok_3: reasons.append("Different set of labels after clicking @ button!")

        test_ok = test_ok_1 and test_ok_2 and test_ok_3

        self.assertTrue(test_ok,
                        f"Error in test_clicking_At_button(self) Reason: {reasons}")

    # No 4 test case in documentation
    # @unittest.skip
    def test_from_lowercase_to_uppercase(self):
        """ Checking whether changing letters from lowercase to uppercase works properly """
        """ Passed if:
        1. word under the picture is in uppercase AND
        2. all scattered labels are in uppercase
        """
        # word and label list BEFORE rising up:
        word_1, labels_list_1 = self.__get_word_and_labels_list()
        # "Rising" the word and labels:
        btn = self.ma.get_upper_lower_button()
        btn.click()
        # Checking after the 'rising':
        word_2, labels_list_2 = self.__get_word_and_labels_list()
        # condition No 1
        test_ok_1 = (word_2 == word_1.upper())
        # condition No 2
        test_ok_2 = True
        for i in range(0, len(labels_list_2)):
            if labels_list_2[i] != labels_list_1[i].upper():
                test_ok_2 = False
                break
        test_ok = test_ok_1 and test_ok_2
        if not test_ok:
            TestUtils.screen_shot(self.driver, "Error while changing letters to uppercase")
        self.assertTrue(test_ok, "Error while changing letters to uppercase. See screenshot.")

    # No 5 test case in documentation
    def test_from_lowercase_to_uppercase_and_back(self):
        """ Checking whether changing letters from lowercase to uppercase and then back to lowercase works properly """
        """ Passed if:
        1. Word under the picture is as it was upon starting the test AND
        2. All scattered labels are as they were upon starting the test
        """
        # word and label list BEFORE rising up:
        word_1, labels_list_1 = self.__get_word_and_labels_list()
        # "Rising" the word and labels:
        btn = self.ma.get_upper_lower_button()
        btn.click()
        # "Lowering" the word and labels
        sleep(1)    # for better visual effect
        btn.click()
        # Checking after the 'Lowering':
        word_2, labels_list_2 = self.__get_word_and_labels_list()
        # condition No 1
        test_ok_1 = (word_2 == word_1)
        # condition No 2
        test_ok_2 = True
        for i in range(0, len(labels_list_2)):
            if labels_list_2[i] != labels_list_1[i]:
                test_ok_2 = False
                break
        test_ok = test_ok_1 and test_ok_2
        if not test_ok:
            TestUtils.screen_shot(self.driver, "Error while changing letters to uppercase and then back to lowercase")
        self.assertTrue(test_ok, "Error while changing letters to uppercase and then back to lowercase. See screenshot.")

    # No 6 test case in documentation
    def test_number_of_labels_is_correct(self):
        """ Passed if the number of scattered letters (labels) equals the length of the guessed word """
        word, labels_list = self.__get_word_and_labels_list()
        num_of_letters = len(word)
        num_of_labels = len(labels_list)
        test_ok = num_of_labels == num_of_letters
        if not test_ok:
            TestUtils.screen_shot(self.driver, "Diffrent numbers of letters and labels")
        self.assertTrue(test_ok, f"Number of labels ({num_of_labels}) on the screen and number"
                                 f"of letters ({num_of_letters}) in the word differ. See screenshot. ")

    # No 7 test case in documentation
    def test_switching_to_settings(self):
        """
        Can switch to Settings?
        Passed if there are checkable elements in the activity we switch to.
        """
        ma = self.ma
        sa = self.sa
        ma.long_touch_on_image()
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(SAL.TITLE))
        list_not_empty = sa.settings_elements_present()
        self.assertTrue(list_not_empty, "Settings did not appear!")

    def __get_word_and_labels_list(self):
        """ Auxiliary. Returns the word under the picture and UNORDERED list of labels (scattered letters) seen on the screen"""
        """ The returned list is list of Strings eg. ['a', 'ż', 'b', 'a'] """
        word = self.ma.get_nazwa_field().text  # the Word under the picture
        labels_id_list = self.ma.get_unordered_list_of_ids_of_shown_labels(MAL.ALL_LABELS_IDS)
        labels_list = []
        for idi in labels_id_list:
            labels_list.append(self.driver.find_element_by_id(idi).text)
        return word, labels_list

    def __move_Labels_to_places(self, labels_list, xo, spacing, ltrim, rnd_range):
        """ Physical moves on labels. Labels from @labels_list are moved to inside of the red box.
        Parameters:
        xo - x position of where to put the FIRST label, then it is modified to place the next one etc.;
        spacing - label width calculated earlier;
        ltrim - horizontal line of 'trim' along which to place the labels;
        rnd_range - the part of the red box height within which the 'dropping' place may by randomly modified;
        """
        for id_el in labels_list:
            ltd = self.driver.find_element_by_id(id_el)  # ltd - label to drag
            action = TouchAction(self.driver)
            rnd_factor = randint(-10, rnd_range)  # only for better visual effect ;)
            action.press(ltd).wait(300).move_to(x=xo, y=ltrim - rnd_factor).perform().release()
            ltd.click()  # trick - only that REALLY releases touch on element
            sleep(0.5)
            xo += spacing

