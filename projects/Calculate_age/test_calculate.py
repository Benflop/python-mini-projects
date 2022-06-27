import unittest

from calculate import *

class TestCalculate(unittest.TestCase):

    def test_judge_leap_year(self):

        # Is Not Leap Year
        isLeapYear = judge_leap_year(1993)
        self.assertEqual(isLeapYear, False)

        # Is Leap Year
        isLeapYear = judge_leap_year(2000)
        self.assertEqual(isLeapYear, True)
    
    def test_months_day(self):

        # 31 Days Month
        months = month_days(1, 1993)
        self.assertEqual(months, 31)

        # 30 Days Month
        months = month_days(4, 1993)
        self.assertEqual(months, 30)

        # Feb in a Leap Year
        months = month_days(2, True)
        self.assertEqual(months, 29)

        # Feb in a Non Leap Year
        months = month_days(2, False)
        self.assertEqual(months, 28)

if __name__ == '__main__':
    unittest.main()