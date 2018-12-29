#import unittest
import unittest

#define / import function
from linear_search import linear_search

#create the class testcase
class LinearSearchTestCase(unittest.TestCase):

    #define the test method
    def test_linear_search(self):
        found = linear_search([1,23,4,5,6,7,6], 5)
        self.assertEqual(3, found)

    def test_linear_search_2(self):
        found = linear_search([1,23,4,5,6,7,6], 6)
        self.assertEqual(4, found)

#make the script executable
if __name__ == '__main__':
    unittest.main()
