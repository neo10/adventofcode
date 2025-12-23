import unittest
import day2

class TestSimple(unittest.TestCase):

    def test_simple(self):
        actual_numbers = []
        expected_numbers = [11,22,99,1010,1188511885,222222,446446,38593859,]
        for bereich in day2.bereiche:
            numbers = range(bereich[0],bereich[1]+1)
            for number in numbers:
                if day2.is_digits_repeated_twice(number):
                    actual_numbers.append(number)
        self.assertListEqual(expected_numbers,actual_numbers)
        print(actual_numbers)
        
