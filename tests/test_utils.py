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

    # @classmethod
    # def prepare_list_of_all_ids_of_labels(cls):
    #     """Regards labels/letters scattered on the screen in MainActivity"""
    #     """Returns list of their identifiers that will later be used in find_element_by_id()"""
    #     """Returned list: [autyzmsoft.pl.literowiec:id/L00,....,autyzmsoft.pl.literowiec:id/L11]"""
    #     labels_list = []
    #     prefix = 'autyzmsoft.pl.literowiec:id/'
    #     for i in range(0, cls.NUM_OF_LABELS):
    #         suffix = str(i)
    #         if i < 10:
    #             lii = prefix + 'L0' + suffix
    #         else:
    #             lii = prefix + 'L' + suffix
    #         labels_list.append(lii)
    #     print("Calość:")
    #     print(labels_list)
    #     # return labels_list
    #     return MainActivityLocators.ALL_LABELS_IDS
    #
    #
    #     # labels_list = \
    #     #     ['autyzmsoft.pl.literowiec:id/L00', 'autyzmsoft.pl.literowiec:id/L01', 'autyzmsoft.pl.literowiec:id/L02',
    #     #      'autyzmsoft.pl.literowiec:id/L03', 'autyzmsoft.pl.literowiec:id/L04', 'autyzmsoft.pl.literowiec:id/L05',
    #     #      'autyzmsoft.pl.literowiec:id/L06', 'autyzmsoft.pl.literowiec:id/L07', 'autyzmsoft.pl.literowiec:id/L08',
    #     #      'autyzmsoft.pl.literowiec:id/L09', 'autyzmsoft.pl.literowiec:id/L10', 'autyzmsoft.pl.literowiec:id/L11']
    #     # # print(labels_list)
    #     # return labels_list
