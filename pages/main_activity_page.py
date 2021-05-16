from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from locators import MainActivityLocators
from tests.test_utils import TestUtils


class MainActivity():

    def __init__(self, sterownik):
        self.driver = sterownik

    def long_touch_on_image(self):
        """Long touching on the image when the image is present"""
        action = TouchAction(self.driver)
        image = self.driver.find_element(*MainActivityLocators.IMAGE)
        action.long_press(image).perform()

    def click_on_image(self):
        image = self.driver.find_element(*MainActivityLocators.IMAGE)
        image.click()

    def get_upper_lower_button(self):
        btn = self.driver.find_element(*MainActivityLocators.BUPPLOW)
        return btn

    def get_nazwa_field(self):
        nazwa = self.driver.find_element(*MainActivityLocators.NAZWA)
        return nazwa

    def __get_unordered_list_of_shown_labels(self, all_labels_ids):
        """Returns a list of ids of labels (=letters) shown on the screen"""
        """Does it by filtering out invisible labels from all_labels_ids list"""

        # speeding up, because it is normal not to find an invisible label
        self.driver.implicitly_wait(0.2)
        ids_of_labels_shown = []
        for id in all_labels_ids:
            try:
                found = self.driver.find_element_by_id(id)
                ids_of_labels_shown.append(id)
            except NoSuchElementException:
                pass
        # restoring timeout:
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)
        # print("ids_of_labels_shown:")
        # print(ids_of_labels_shown, len(ids_of_labels_shown))
        return ids_of_labels_shown

    def __get_first_index_of_an_elem_containing_letter(self, lista, litera):
        dl = len(lista)
        for i in range(0, dl):
            zawartosc = self.driver.find_element_by_id(lista[i]).text
            if zawartosc == litera:
                return i
        return -1

    def get_ordered_list_of_shown_labels(self, word):
        """Returns the list of IDs of all visible labels (=letters)"""
        """The returned list is of the same sequence as the letters in 'word' are. """
        result = []
        ul = self.__get_unordered_list_of_shown_labels(MainActivityLocators.ALL_LABELS_IDS)
        # Iterating through 'word' (from left to right) guarantees that the resultant list
        # will have the same sequence as the letters in 'word'
        for letter in word:
            idx = self.__get_first_index_of_an_elem_containing_letter(ul, letter)
            result.append(ul[idx])
            # The element just found MUST be removed from the list, otherwise if the word contains many same
            # letters, only the first one would be kept finding:
            ul.pop(idx)
        return result
        # print(result)
        # for x in result:
        #     labelka = self.driver.find_element_by_id(x)
        #     print(labelka.text)


