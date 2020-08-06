""" Tests for lambdata modules"""

import unittest
import pandas as pd
import numpy as np
from random import randint
from package0 import data_null_check
from package1 import Car


class TestPackage0(unittest.TestCase):
    """Testing functions work as expected in Package0"""
    def test_data_null_check(self):
        """Tests if the correct # of nulls for data_null_check are returned"""
        NaN = np.NaN
        df1 = pd.DataFrame({'a': [NaN, 3, 4, 5], 'b': [1, NaN, 5, 7]})
        df2 = pd.DataFrame({'b': [NaN, 7, 8, 9, 10]})df2 = pd.DataFrame({'b': [NaN, 7, 8, 9, 10]})
        self.assertEqual(sum(data_null_check(df1).values), 2)
        self.assertEqual(sum(data_null_check(df2).values), 1)


class TestPackage1(unittest.TestCase):
    """Testing in classes in package1's methods and attributes work as expected"""

    def test_Car(self):
        """Test if the methods in Car work as they should"""
        car = Car(100, 200, 10000, color='yellow')
        sound1 = car
        self.assertEqual(car.sound(), "ROOOM")


if __name__ == '__main__':
    unittest.main()
