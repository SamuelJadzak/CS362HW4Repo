import unittest
import fullNameGen

class testcase1(unittest.TestCase):
    def test_integers(self):
        result = fullNameGen.nameGen("Bobby","Pantalone")
        self.assertEqual(result, "Bobby Pantalone")
    
    def test_emptylastname(self):
        result = fullNameGen.nameGen("Bobby","")
        self.assertEqual(result, "Bobby")

    def test_zeroList(self):
        self.assertRaises(ValueError, fullNameGen.nameGen, 1, "")
    
if __name__ == '__main__':
    unittest.main()