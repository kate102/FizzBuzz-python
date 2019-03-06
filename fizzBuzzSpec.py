import unittest

from fizzBuzz import *

class MyFirstTest(unittest.TestCase):

  def test_hello(self):
    self.assertEqual(isFizz(3), 'Fizz')

class MySecondTest(unittest.TestCase):
  def test_hello(self):
    self.assertEqual(isFizz(5), 'Buzz')

class MyThirdTest(unittest.TestCase):
  def test_hello(self):
    self.assertEqual(isFizz(15), 'FizzBuzz')

class MyForthTest(unittest.TestCase):
  def test_hello(self):
    self.assertEqual(isFizz(7), 7)

if __name__ == '__main__':
   unittest.main()
