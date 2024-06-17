import unittest
from utils.utils import find_key_length

class TestFindKeyLength(unittest.TestCase):
    def test_typical_case(self):
        test_cases = {
            "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ": 26,
            "ABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDE": 5,
            "ABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABC": 3
        }

        for test_string, expected in test_cases.items():
            byte_array = bytearray(test_string, "utf-8")
            with self.subTest(byte_array=byte_array):
                result = find_key_length(byte_array)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()