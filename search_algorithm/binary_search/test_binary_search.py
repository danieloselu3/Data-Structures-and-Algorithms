#import unittest
import unittest

#import binary_search
from binary_search import binary_search

#create class test case
class BinarySearchTestCase(unittest.TestCase):

    #define the test method
    def test_binary_search(self):
        found = binary_search([1,3,4,5,6,7,8,9,12,23,24,27,35,38,157], 35)
        self.assertEqual(True, found)

    def test_binary_search_2(self):
        found = binary_search([1,3,4,5,6,7,8,9,12,23,24,27,35,38,157], 2)
        self.assertEqual(False, found)

    def test_binary_search_3(self):
        found = binary_search([1,3,4,5,6,7,8,9,12,23,24,27,35,38,157], 3)
        self.assertEqual(True, found)

#make our script executable
if __name__ == '__main__':
    unittest.main()
