import CH05.exo1
import unittest

class TestExo1(unittest.TestCase):
  def test_push(self):
    output = CH05.exo1.Stack('myStack')
    self.assertEqual(output.push('first element').top(), 'first element')

  def test_pop(self):
    output = CH05.exo1.Stack('myStack')
    self.assertEqual(
      output
        .push('first element')
        .push('second element')
        .pop()
        .top()
      , 'first element')

if __name__ == '__main__':
  unittest.main()
