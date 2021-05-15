from appium.webdriver.common.touch_action import TouchAction

from locators import MainActivityLocators


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
