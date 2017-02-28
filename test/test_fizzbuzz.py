import unittest
from fizzbuzz import *


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_fizzbuzz(self):
        model = FizzBuzzModel()
        self.assertEquals(self.__solution(), model.solve())

    @staticmethod
    def __solution():
        solution = []
        for num in xrange(1, 201):
            msg = ''
            if num % 3 == 0:
                msg += 'fizz'
            if num % 5 == 0:
                msg += 'buzz'
            if num % 7 == 0:
                msg += 'pop'
            solution.append(msg or str(num))

        return solution
