# coding: utf-8
import unittest


# problem3
class Problem3:
    def generate_string(self, n):
        if n == 0:
            return []
        if n == 1:
            return ['0', '1']
        if n != 1:
            first = ['1' + i for i in self.generate_string(n - 1)]
            zero = ['0' + i for i in self.generate_string(n - 1)]
            return first + zero

    def generate_string1(self, n):
        if n == 0:
            return []
        if n == 1:
            return ['0', '1']
        return [digit + string for digit in self.generate_string1(1) for string in self.generate_string1(n - 1)]


if __name__ == '__main__':
    class TestProblem3(unittest.TestCase):
        def test_checks_gerated_string_length(self):
            string = Problem3().generate_string(4)
            self.assertTrue(len(string) == 2 ** 4)
            self.assertTrue('1111' in string)


    print(Problem3().generate_string(4))
    unittest.main()
