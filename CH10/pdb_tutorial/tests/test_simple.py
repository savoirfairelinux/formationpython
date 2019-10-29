import unittest
from CH10.pdb_tutorial.dicegame.die import Die

scope = 2

class TestStringMethods(unittest.TestCase):

    def setup(self):
        self.die = Die()
        self.die.roll()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


    def test_scope(self):
        myDic = {
          'something': 1,
          'something_else': 'haha'
        }

        print(myDic[])
        # scope = 2
        # def myFunc():
        #     scope = 5
        # myFunc()
        # if True:
        #     scope = 6
        self.assertEqual(scope, 5)

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
