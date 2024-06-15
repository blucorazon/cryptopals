import unittest
from utils import hamming_distance

class TestHammingDistance(unittest.TestCase):
    def test_hamming_distance(self):
        test_cases = {
            ("this is a test", "wokka wokka!!!"): 37
        }

        for (str1, str2), expected in test_cases.items():
            with self.subTest(str1=str1, str2=str2):
                result = hamming_distance(str1, str2)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()