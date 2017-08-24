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


# R-5.1 C-5.13
def experiment_list_length_origin(n, data=[]):
    import sys
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(None)


# R-5.2 C-5.13
def experiment_list_length_amend(n, data=[]):
    import sys
    a = 0
    b = 0
    for k in range(n):
        l = len(data)
        m = sys.getsizeof(data)
        if m != b and b != 0:
            print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        a, b = l, m
        data.append(None)


# R-5.3
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


# R-5.4 R-5.6
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
            B = self._make_array(2 * self._capacity)
            for j in range(k):
                B[j] = self._A[j]
                self._A = B
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1


# R-5.7
def find_repeated_int(arr):
    temp = 0
    for i in arr:
        if i == temp:
            return i
        temp = i


# R-5.8
def compute(n):
    from time import time
    start = time()
    data = [None] * n
    for i in range(n):
        data.pop()
    end = time()
    return (end - start) / n


# R-5.10
class CaesarCipher(object):
    def __init__(self, shift):
        self._forward = ''.join([chr((k + shift) % 26 + ord('A')) for k in range(26)])
        self._backward = ''.join([chr((k - shift) % 26 + ord('A')) for k in range(26)])


# R-5.11
def compute_data_set_sum(data_set):
    sum = 0
    for i in data_set:
        for j in i:
            sum += j
    return sum


# R-5.12
def compute_data_set_sum1(data_set):
    return sum([j for i in data_set for j in i])


# C-5.1
# def


if __name__ == '__main__':
    # print experiment_list_length_origin(27)
    # print experiment_list_length_origin(27, [1, 2, 3])
    print experiment_list_length_amend(29)
    print experiment_list_length_amend(27, [1])
    print experiment_list_length_amend(27, [1]*2)
    print experiment_list_length_amend(27, [1]*3)
    print experiment_list_length_amend(27, [1]*4)
    # print compute_data_set_sum1([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    # print CaesarCipher(1)._forward
    # print CaesarCipher(1)._backward
    # for i in [100, 1000, 10000, 100000, 1000000]:
    #     print compute(i)
    # print find_repeated_int([1, 2, 3, 3, 4, 5])
    # experiment_list_length_amend1(27)
    # experiment_list_length_amend(27)
    # experiment_list_length_origin(27)
    # print insertion_sort([3, 2, 5, 1])
