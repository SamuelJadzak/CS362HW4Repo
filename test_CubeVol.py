import unittest
import CubeVolume

class testcase2(unittest.TestCase):
    def test_integer(self):
        result = CubeVolume.cubeVol(3)
        self.assertEqual(result, 27)
    
    def test_zeroInt(self):
        self.assertRaises(ValueError, CubeVolume.cubeVol, 0)

    def test_characterInput(self):
        self.assertRaises(ValueError, CubeVolume.cubeVol, "a") 


if __name__ == '__main__':
    unittest.main()