from __future__ import print_function
from helper import unittest, PillowTestCase

from PIL2 import Image

import locale

# ref https://github.com/python-pillow/Pillow2/issues/272
# on windows, in polish locale:

# import locale
# print(locale.setlocale(locale.LC_ALL, 'polish'))
# import string
# print(len(string.whitespace))
# print(ord(string.whitespace[6]))

# Polish_Poland.1250
# 7
# 160

# one of string.whitespace is not freely convertable into ascii.

path = "Tests/images/hopper.jpg"


class TestLocale(PillowTestCase):

    def test_sanity(self):
        Image.open(path)
        try:
            locale.setlocale(locale.LC_ALL, "polish")
        except locale.Error:
            unittest.skip('Polish locale not available')
        Image.open(path)


if __name__ == '__main__':
    unittest.main()
