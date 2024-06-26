import unittest
from utils.utils import hamming_distance

class TestHammingDistance(unittest.TestCase):
    def test_hamming_distance(self):
        test_cases = {
            (b"this is a test", b"wokka wokka!!!"): 37,
            (b"a", b"d"): 2
        }

        for (str1, str2), expected in test_cases.items():
            with self.subTest(str1=str1, str2=str2):
                result = hamming_distance(str1, str2)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()