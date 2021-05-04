import unittest
import listAverage

class testcase1(unittest.TestCase):
    def test_integers(self):
        result = listAverage.listAvg([1,2,3,4])
        self.assertEqual(result, 2.5)
    
    def test_nullList(self):
        self.assertRaises(ValueError, listAverage.listAvg, [])

"""     def test_zeroList(self):
        result = listAverage.listAvg([0])
        self.assertEqual(result, 0) """

if __name__ == '__main__':
    unittest.main()