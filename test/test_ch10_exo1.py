from CH10.pdb_tutorial.dicegame.runner import GameRunner
import unittest

class TestExo2(unittest.TestCase):
  def test_somthing(self):
    output = GameRunner.run()
    self.assertEqual(output, [[1,2,3], [2,3,4]])

if __name__ == '__main__':
  unittest.main()
