class ListArray():
    @classmethod
    def sum(cls, a_list):
        res = 0
        for i in a_list:
            res += i
        return res

    @classmethod
    def search(cls, a_list, value):
        for i in a_list:
            if i == value:
                return True
        return False

    @classmethod
    def bi_search(cls, a_list, value):
        length = len(a_list)
        left = 0
        right = length - 1
        while right >= left:
            mid = (left + right) // 2
            test = a_list[mid]
            if test > value:
                right = mid + 1
            elif test < value:
                left = mid + 1
            elif test == value:
                return True
        return False

    @classmethod
    def rotate(cls, a_list, pos):
        res = a_list[pos:] + a_list[:pos]
        return res

    @classmethod
    def rotate_array(cls, arr, k):
        n = len(arr)
        cls.reverse_array(arr, 0, k - 1)
        cls.reverse_array(arr, k, n - 1)
        cls.reverse_array(arr, 0, n - 1)

    @classmethod
    def reverse_array(cls, arr, start, end):
        i = start
        j = end
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    @classmethod
    def find_largest_contiguous_subarray(cls, arr):
        length = len(arr)
        left = 0
        res_sum = arr[0]
        res_arr = [arr[0]]
        while left < length:
            right = left
            temp_arr = []
            while right < length:
                temp_arr.append(arr[right])
                test = sum(temp_arr)
                if test > res_sum:
                    res_sum = test
                    res_arr = temp_arr
                right += 1
            left += 1
        return res_arr

    @classmethod
    def maxSubArraySum(cls, arr):
        size = len(arr)
        maxSorFar = 0
        maxEndingHere = 0
        i = 0
        while i < size:
            maxEndingHere += arr[i]
            if maxEndingHere < 0:
                maxEndingHere = 0
            if maxSorFar < maxEndingHere:
                maxSorFar = maxEndingHere
            i += 1
        return maxSorFar

    @classmethod
    def factorial(cls, i):
        if i <= 1:
            return 1
        elif i > 1:
            return i * cls.factorial(i - 1)

    @classmethod
    def GCD(cls, m, n):
        if m > n:
            return cls.GCD(n, m)
        if m % n == 0:
            return n
        return cls.GCD(n, m % n)

    @classmethod
    def fibonacci(cls, n):
        if n <= 1:
            return n
        return cls.fibonacci(n - 1) + cls.fibonacci(n - 2)

    @classmethod
    def binary_search(cls, arr, value, low, high):
        mid = (low+high) // 2
        if low > high:
            return False
        if arr[mid] == value:
            return mid
        elif value > arr[mid]:
            return cls.binary_search(arr, value, mid + 1, high)
        elif value < arr[mid]:
            return cls.binary_search(arr, value, low, mid - 1)


if __name__ == '__main__':
    print ListArray.binary_search([2], 2, 0, 0)
    print ListArray.binary_search([1, 2], 2, 0, 1)
    print ListArray.binary_search([1, 2, 3, 7, 10], 2, 0, 4)
    print ListArray.binary_search([1, 2, 3, 7, 10], 12, 0, 4)
    print ListArray.binary_search([1, 2, 3], 7, 0, 2)
    # print ListArray.factorial(5)
    # print ListArray.find_largest_contiguous_subarray([-1, -3, 5, 7, 2, -10, 3, 5, 7])
    # print ListArray.find_largest_contiguous_subarray([-1, -3, 5, 7, 2, -10, 3, 5, 7, -6, 8, -1])
    # print ListArray.find_largest_contiguous_subarray([0, -1])
    # print ListArray.find_largest_contiguous_subarray([-1, 0])
    # print ListArray.find_largest_contiguous_subarray([1, -2, 3, 4, -4, 6, -4, 8, 2])
    # print ListArray.maxSubArraySum([-1, -2])
    # print ListArray.maxSubArraySum([-1, -2, 3, -4, 10, -3, 11])
    # print ListArray.bi_search([2], 2)
    # print ListArray.bi_search([1, 2], 2)
    # print ListArray.bi_search([1, 2, 3, 7, 10], 2)
    # print ListArray.bi_search([1, 2, 3, 7, 10], 12)
    # print ListArray.bi_search([1, 2, 3], 7)
