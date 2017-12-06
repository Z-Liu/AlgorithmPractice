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


class TestProblem3(unittest.TestCase):
    def test_checks_generated_string(self):
        string_list = Problem3().generate_string(4)
        self.assertEqual(len(string_list), 2 ** 4)
        self.assertTrue('1111' in string_list)


class Problem4:
    def generate_string(self, n, k):
        if n == 0:
            return []
        if n == 1:
            return [str(i) for i in range(k)]
        return [str(i) + j for i in range(k) for j in self.generate_string(n - 1, k)]


class TestProblem4(unittest.TestCase):
    def test_checks_generated_string(self):
        string_list = Problem4().generate_string(10, 2)
        self.assertEqual(len(string_list), 2 ** 10)


class Problem6:
    maxsize = 0

    def __init__(self, cntarr):
        self.cntarr = cntarr

    def getval(self, A, i, j, L, H):
        if i < 0 or i >= L or j < 0 or j >= H:
            return 0
        else:
            return A[i][j]

    def findMaxBlock(self, A, r, c, L, H, size):
        if r >= L or c >= H:
            return
        self.cntarr[r][c] = True  # cntarr用于标记某位置在本次测试中是否被测试过
        size += 1
        if size > self.maxsize:
            self.maxsize = size
        direction = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
        for i in range(7):
            newi = r + direction[i][0]
            newj = c + direction[i][1]
            val = self.getval(A, newi, newj, L, H)
            if val > 0 and self.cntarr[newi][newj] is False:
                self.findMaxBlock(A, newi, newj, L, H, size)
        self.cntarr[r][c] = False

    def getMaxOnes(self, A, rmax, colmax):
        for i in range(rmax):
            for j in range(colmax):
                if A[i][j] == 1:
                    self.findMaxBlock(A, i, j, rmax, colmax, 0)
        return self.maxsize


class TestProblem6(unittest.TestCase):
    def test_solution(self):
        zarr = [[1, 1, 0, 0, 0], [0, 1, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 1, 1], [0, 1, 0, 1, 1]]
        rmax = 5
        colmax = 5
        problem = Problem6(rmax * [colmax * [False]])
        res = problem.getMaxOnes(zarr, rmax, colmax)
        print(res)


if __name__ == '__main__':
    unittest.main()
