# project Literowiec_POM
<p>
Automatic tests of some functionalities of <strong><em>&nbsp;Literowiec&nbsp;</em></strong> android application.<br>
Page Object Model and simple Data-driven testing are applied.
</p>
<p>
Most convenient usage:&nbsp;&nbsp;<em><strong>python3 suite_raport.py</strong></em><br>
Html reports are placed in <em>test_results</em> in the default directory
</p>

### Dependencies
java 1.8\
Android Studio 4.1.2\
node.js 14.16.0\
npm 6.14.11\
appium 1.20.2\
appium-doctor 1.16.0\
Pycharm 2021.1\
python 3.8.5\
pip 21.0.1\
Appium Python Client 1.1.1\
selenium 3.141.0\
ddt 1.4.2\
html-testRunner 1.2.1
<h2>List of test cases</h2>
Totals: 9 test cases<br>
Order: as they appear in the source code<br>
<hr>
1<br>
<strong>def test_build_the_word(self, placeholder):</strong><br>
"""Passed if:<br>
 1. There appears element WORD_BUILT containing the word we built manually from the labels/letters AND<br>
 2. WORD_BUILT properly describes the picture AND<br>
 3. There appears on the screen a big button with green arrow<br>
 """
<hr>
2<br>
<strong>def test_build_the_word_incorrectly(self):</strong><br>
""" What happens after we've built the word incorrectly. """<br>
Passed if:<br>
1. All labels are placed in the red box in such a way that they do not form the proper word AND<br>
2. The big button with green arrow do NOT appear<br>
"""
<hr>
3<br>
<strong>def test_clicking_At_button(self):</strong><br>
""" What happens after we click @ button?<br>
Passed if:<br>
1. The word under the picture does not change AND<br>
2. Labels scattered on the screen do change their positions AND<br>
3. Labels contain the same set of letters as before<br>
"""
<hr>
4<br>
<strong>def test_from_lowercase_to_uppercase(self):</strong><br>
""" Checking whether changing letters from lowercase to uppercase works properly.<br>
Passed if:<br>
1. word under the picture is in uppercase AND<br>
2. all scattered labels are in uppercase<br>
"""
<hr>
5<br>
<strong>def test_from_lowercase_to_uppercase_and_back(self):</strong><br>
""" Checking whether changing letters from lowercase to uppercase and then back to lowercase works properly.<br>
Passed if:<br>
1. Word under the picture is as it was upon starting the test AND<br>
2. All scattered labels are as they were upon starting the test<br>
"""
<hr>
6<br>
<strong>def test_number_of_labels_is_correct(self):</strong><br>
""" Passed if:<br>
- the number of scattered letters (labels) equals the length of the guessed word<br>
"""
<hr>
7<br>
<strong>def test_switching_to_settings(self):</strong><br>
""" Can switch to Settings?<br>
Passed if:<br>
- there are checkable elements in the activity we switch to.<br>
"""
<hr>
8<br>
<strong>def test_switching_off_word_and_picture(self):</strong><br>
""" Is switching off the picture and the word (nazwa) under the picture effective?<br>
Passed if:<br>
1. Picture is not visible AND<br>
2. Word under the picture is not visible<br>
"""
<hr>
9<br>
<strong>def test_switching_to_info_activity(self):</strong><br>
""" Can switch to Info?<br>
Passed if:<br>
1. there is "android:id/action_bar_title element in the activity we switch to AND<br>
2. it contains "Informacje o aplikacji" text<br>
<p>&nbsp;</p>




