class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
            self._A = B
            self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError('value not found')


from time import time


def compute_average(n):
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n


class GameEntry(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)


class Scoreboard(object):
    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        return self._board[k]

    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry


def insertion_sort(arr):
    i = 1
    while i < len(arr):
        j = i
        temp = arr[j]
        while j > 0 and arr[j - 1] > temp:
            arr[j] = arr[j - 1]
            j -= 1
        i += 1
        arr[j] = temp
    return arr


def experiment_list_length_origin(n):
    import sys
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(None)


def experiment_list_length_amend(n):
    import sys
    data = []
    a = 0
    b = 0
    for k in range(n):
        l = len(data)
        m = sys.getsizeof(data)
        if m != b and b != 0:
            print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        a, b = l, m
        data.append(None)


def experiment_list_length_amend1(n):
    import sys
    data = [None] * n
    a = 0
    b = 0
    for k in range(n):
        l = len(data)
        m = sys.getsizeof(data)
        if m != b and b != 0:
            print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        a, b = l, m
        data.pop()


import ctypes


class DynamicArray(object):
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            i = k % self._n
            return self._A[i]
        # raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        if self._n == self._capacity:
            B = self._make_array(2*self._capacity)
            for j in range(k):
                B[j] = self._A[j]
                self._A = B
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1


if __name__ == '__main__':
    # experiment_list_length_amend1(27)
    experiment_list_length_amend(27)
    # experiment_list_length_origin(27)
    # print insertion_sort([3, 2, 5, 1])
