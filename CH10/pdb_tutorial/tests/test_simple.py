import io
import sys
import unittest

from CH10.pdb_tutorial.dicegame.runner import GameRunner
from ..dicegame.die import Die


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        die = Die()
        die.roll()

    def test_input(self):
        """
        Test that the prompt accepts y/Y and n/N
        :return:
        """
        game_runner = GameRunner()

        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.

        runner = game_runner.run(guess='5', prompt='y')

        output = captured_output.getvalue()
        self.assertTrue("You won... Congrats..." in output)
        self.assertTrue("Round 1" in output)
        self.assertTrue("Round 2" in output)
        self.assertTrue("Round 3" in output)
        self.assertTrue("Round 4" in output)
        self.assertTrue("Round 5" in output)
        self.assertTrue("Round 6" in output)
        self.assertEqual(runner.loses, 6)
        self.assertEqual(runner.round, 7)  # 7 because not zero based

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
