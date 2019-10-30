from CH10.pdb_tutorial.dicegame.runner import GameRunner
import unittest
import unittest.mock

class TestExo2(unittest.TestCase):
  def test_somthing(self):
    with unittest.mock.patch('builtins.input', return_value='1'):
      output = GameRunner.run()

if __name__ == '__main__':
  unittest.main()
