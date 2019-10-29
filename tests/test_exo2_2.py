import CH02.exo2_2
import unittest

class TestExo2(unittest.TestCase):
  def test_somthing(self):
    output = CH02.exo2_2.myFunction([1,2,3,4])
    self.assertEqual(output, [[1,2,3], [2,3,4]])

if __name__ == '__main__':
  unittest.main()
