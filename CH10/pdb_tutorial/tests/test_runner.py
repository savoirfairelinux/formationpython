import unittest
from CH10.pdb_tutorial.dicegame.runner import GameRunner


class TestStringMethods(unittest.TestCase):

    def setup(self):
        pass

    def test_Y(self):
        gr = GameRunner.run(4, 'Y')
        self.assertEqual(gr.loses, 6)


if __name__ == '__main__':
    unittest.main()
