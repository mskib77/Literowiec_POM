import os
from datetime import datetime


class TestUtils:
    WAIT_TIME = 10  # system-wide implicit wait
    NUM_OF_LABELS = 12  # max number of letters (=named 'LabesNN' in Android Studio) in guessed word

    @classmethod
    def screen_shot(cls, driver, file_name):
        time_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        store_file = f'{os.getcwd()}/screenshots/' + time_now + '_' + file_name + '.png'
        # print(f"Sciezka: {store_file}")
        driver.get_screenshot_as_file(store_file)

    @classmethod
    def get_screen_dimensions(cls, driver):
        """ Used before we start scrolling """
        size: dict = driver.get_window_size()
        x = size['width']
        y = size['height']
        return x, y

    @classmethod
    def prepare_list_of_all_labels_ids(cls):
        """Returns list of identifiers used in find_element()"""
        """IDs refer to letters scattered on the screen in Main Activity"""
        """Returnd list [autyzmsoft.pl.literowiec:id/L00,....,autyzmsoft.pl.literowiec:id/L11]"""
        labels_list = []
        prefix = 'autyzmsoft.pl.literowiec:id/'
        for i in range(0, cls.NUM_OF_LABELS):
            suffix = str(i)
            if i < 10:
                lii = prefix + 'L0' + suffix
            else:
                lii = prefix + 'L' + suffix
            labels_list.append(lii)
        return labels_list
