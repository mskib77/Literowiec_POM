from selenium.webdriver.common.by import By


class MainActivityLocators:
    IMAGE = (By.ID, 'autyzmsoft.pl.literowiec:id/imageView')
    # Name under the picture. Later in code referred to as 'word', 'guessed word', proper word', 'nazwa' etc.:
    NAZWA = (By.ID, 'autyzmsoft.pl.literowiec:id/tvNazwa')
    BUPPLOW = (By.ID, 'autyzmsoft.pl.literowiec:id/bUpperLower')
    BDALEJ = (By.ID, 'autyzmsoft.pl.literowiec:id/bDalej')
    OBSZAR = (By.ID, 'autyzmsoft.pl.literowiec:id/l_Obszar')
    BSHIFT_LEFT = (By.ID, 'autyzmsoft.pl.literowiec:id/bShiftLeft')
    B_AGAIN = (By.ID, 'autyzmsoft.pl.literowiec:id/bAgain')
    # Word that appears in the 'red box' AFTER (only) we correctly did the puzzle:
    WORD_BUILT = (By.ID, 'autyzmsoft.pl.literowiec:id/tvShownWord')

    L00_str = 'autyzmsoft.pl.literowiec:id/L00'
    L01_str = 'autyzmsoft.pl.literowiec:id/L01'
    L02_str = 'autyzmsoft.pl.literowiec:id/L02'
    L03_str = 'autyzmsoft.pl.literowiec:id/L03'
    L04_str = 'autyzmsoft.pl.literowiec:id/L04'
    L05_str = 'autyzmsoft.pl.literowiec:id/L05'
    L06_str = 'autyzmsoft.pl.literowiec:id/L06'
    L07_str = 'autyzmsoft.pl.literowiec:id/L07'
    L08_str = 'autyzmsoft.pl.literowiec:id/L08'
    L09_str = 'autyzmsoft.pl.literowiec:id/L09'
    L10_str = 'autyzmsoft.pl.literowiec:id/L10'
    L11_str = 'autyzmsoft.pl.literowiec:id/L11'

    # list of ALL labels ids, including those that are currently not visible on the screen
    # (invisible because the guessed word does not include so many letters):
    ALL_LABELS_IDS = [L00_str, L01_str, L02_str, L03_str, L04_str, L05_str,
                      L06_str, L07_str, L08_str, L09_str, L10_str, L11_str]



class SettingsActivityLocators:
    TITLE = (By.ID, 'autyzmsoft.pl.literowiec:id/tv_tytul')
    CB_NAZWA_ID = 'autyzmsoft.pl.literowiec:id/cb_Nazwa'
    RB_NOPICTURE_ID = 'autyzmsoft.pl.literowiec:id/rb_noPicture'
    BINFO_ID = 'autyzmsoft.pl.literowiec:id/bInfo'

class InfoActivityLocators:
    ACTION_BAR_TITLE = (By.ID, 'android:id/action_bar_title')