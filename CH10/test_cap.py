import sys
print(sys.path)

import unittest
from .cap import cap_text


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'toto'
        result = cap_text(text)
        self.assertEqual(result, 'TOTO')

if __name__ == '__main__':
    unittest.main()
