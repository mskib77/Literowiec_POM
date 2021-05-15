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

    def get_unordered_list_of_shown_labels(self):
        all_labels = TestUtils.prepare_list_of_all_labels_ids()
        # speeding up, because it is normal not to found invisible label
        self.driver.implicitly_wait(0.2)
        labels_shown = []
        for label in all_labels:
            try:
                found = self.driver.find_element_by_id(label)
                labels_shown.append(label)
            except NoSuchElementException:
                pass
        # restoring timeout:
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)
        print("labels_shown:")
        print(labels_shown, len(labels_shown))
        return labels_shown
