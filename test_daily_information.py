import unittest
from daily_information import *

class Test_Daily_Information(unittest.TestCase):

    def setUp(self):
        self.information = Daily_Information('2015-09-04', 'valor_cuota_diaria.xls')

    def test_init(self):
        self.assertIsInstance(self.information, Daily_Information, 'is a Daily_Information object')

        self.assertEqual(self.information.year, 2015, 'checking year')
        self.assertEqual(self.information.month, 9, 'checking month')
        self.assertEqual(self.information.day, 4, 'checking day')

    def test_load_information(self):
        self.assertTrue(self.information.load_information(), 'Load information')

    def test_show_information(self):
        self.assertIsInstance(self.information.get_information(), list, 'datatype information')



if __name__ == '__main__':
    unittest.main()
