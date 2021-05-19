from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from locators import MainActivityLocators
from tests.test_utils import TestUtils


class MainActivity:

    def __init__(self, sterownik):
        self.driver = sterownik

    def long_touch_on_image(self):
        """Long touching on the image when the image is present"""
        action = TouchAction(self.driver)
        image = self.driver.find_element(*MainActivityLocators.IMAGE)
        action.long_press(image).perform()

    def get_upper_lower_button(self):
        btn = self.driver.find_element(*MainActivityLocators.BUPPLOW)
        return btn

    def get_nazwa_field(self):
        nazwa = self.driver.find_element(*MainActivityLocators.NAZWA)
        return nazwa

    def get_unordered_list_of_ids_of_shown_labels(self, all_labels_ids):
        """Returns a list of ids of labels (=letters) shown scattered on the screen"""
        """Does it by filtering out invisible labels from all_labels_ids list"""

        # speeding up, because it is normal not to find an invisible label
        self.driver.implicitly_wait(0.2)
        # Trying to find labels on the screen; if not found - that's ok, it is simply not used so it's invisible
        # (eg. the guessed Word is too short to occupy all the labels etc.):
        ids_of_labels_shown = []
        for idi in all_labels_ids:
            try:
                found = self.driver.find_element_by_id(idi)
                ids_of_labels_shown.append(idi)
            except NoSuchElementException:
                pass
        # restoring timeout:
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)
        return ids_of_labels_shown

    def __get_first_index_of_an_elem_containing_letter(self, lista, litera):
        dl = len(lista)
        for i in range(0, dl):
            zawartosc = self.driver.find_element_by_id(lista[i]).text
            if zawartosc == litera:
                pass
                return i
        raise Exception(
            "\nError in function MainActivity.__get_first_index_of_an_elem_containing_letter(self, lista, litera)"
            "\nIndex not found")

    def get_ordered_list_of_ids_of_shown_labels(self, word):
        """Returns the list of IDs of all visible labels (=letters)"""
        """The returned list is of the same sequence as the letters in 'word' are. """
        result = []
        ul = self.get_unordered_list_of_ids_of_shown_labels(MainActivityLocators.ALL_LABELS_IDS)
        # Iterating through 'word' (from left to right) guarantees that the resultant list
        # will have the same sequence as the letters in 'word'
        for letter in word:
            idx = self.__get_first_index_of_an_elem_containing_letter(ul, letter)
            result.append(ul[idx])
            # The element just found MUST be removed from the list, otherwise if the word contains more same
            # letters, only the first letter (=label) would be kept finding:
            ul.pop(idx)
        return result

    def get_word_built(self):
        try:
            wb = self.driver.find_element(*MainActivityLocators.WORD_BUILT)
            return wb
        except NoSuchElementException:
            return -1

    def get_bdalej_button(self):
        try:
            btn = self.driver.find_element(*MainActivityLocators.BDALEJ)
            return btn
        except NoSuchElementException:
            return -1

    def get_dimensions(self, seen_labels_ids):
        """Used in doing the puzzle to properly (physical coordinates) place labels (=letters) in the red box """
        """Returns:
         'average' label/letter width;
         left (x0) position to place the first letter in the box;
         (yl) line of trim (along which the letters should be aligned);
         box_height (red box height);
         """
        # label/letter width taken as average of 2 first labels (heuristic approach ;))
        ltd_0 = self.driver.find_element_by_id(seen_labels_ids[0])
        # almost improbable (1 letter word), but... :
        if len(seen_labels_ids) > 1:
            ltd_1 = self.driver.find_element_by_id(seen_labels_ids[1])
        else:
            ltd_1 = ltd_0
        sizes_0 = ltd_0.size
        sizes_1 = ltd_1.size
        l_width = int((sizes_0.get('width') + sizes_1.get('width')) / 2)
        # left position x0 of the first letter being set and the horizontal line of trim (yl):
        red_box = self.driver.find_element(*MainActivityLocators.OBSZAR)
        red_box_location = red_box.location
        red_box_sizes = red_box.size
        x0 = red_box_location.get('x')
        box_h = red_box_sizes.get('height')
        # print("box_h: ", box_h)
        # print("drugi wymiar: ", red_box_sizes.get('width'))
        yl = red_box_location.get('y') + int(box_h / 2)
        # print("x0 l_width yl box_h: ", x0, l_width, yl, box_h)
        return l_width, x0, yl, box_h
