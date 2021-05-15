import os
import unittest
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.main_activity_page import MainActivity
from tests.test_utils import TestUtils

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """

    def setUp(self):
        print("setUp z BaseTest")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'

        desired_caps['deviceName'] = 'emulator-554'
        # desired_caps['deviceName'] = '5210f505ea6b8467' # moj nowy telefon
        # desired_caps['deviceName'] = '5200241cea6f7523'   # moj Stary telefon

        desired_caps['app'] = PATH('Literowiec.apk')
        desired_caps['appPackage'] = 'autyzmsoft.pl.literowiec'
        desired_caps['appActivity'] = 'autyzmsoft.pl.literowiec.MainActivity'
        desired_caps['autoGrantPermissions'] = 'true'

        desired_caps['automationName'] = 'UiAutomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.update_settings({"allowInvisibleElements": True})
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)

        self.__dismiss_splash_window()

        self.create_activities()

    def create_activities(self):
        """ SUT objects (=activities) creation """
        " These activities will/may be used by tests "
        self.ma = MainActivity(self.driver)
        # self.sa = SettingsActivity(self.driver)
        # self.ia = InfoActivity(self.driver)

    def __dismiss_splash_window(self):
        """ Clicks on OK to unlock Main Activity """
        """ Note: OK button may not be visible on some devices, therefore scrolling """

        x, y = TestUtils.get_screen_dimensions(self.driver)
        # speeding up a little:
        self.driver.implicitly_wait(1)
        # scrolling down till the INFO button appears:
        found = False
        while not found:
            try:
                el = self.driver.find_element(By.ID, "autyzmsoft.pl.literowiec:id/btn_OK")
                found = True
                el.click()
            except NoSuchElementException:
                self.driver.swipe(x/2, y/2, x/2, y/7, 500)
        # restoring timeout:
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)


    def tearDown(self):
        print("tearDown z BaseTest")
        self.driver.quit()
