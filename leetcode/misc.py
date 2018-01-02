# coding: utf-8
# https://leetcode.com/problems/sum-of-two-integers/description/
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return eval('%s+%s' % (str(a), str(b)))


# https://leetcode.com/problems/missing-number/description/
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        alist = [False] * (len(nums) + 1)
        for i in nums:
            alist[i] = True
        res = 0
        for i in alist:
            if i is False:
                return res
            res += 1

    def missingNumber1(self, nums):
        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0
        for i in range(1, len(nums)):
            expected_num = nums[i - 1] + 1
            if nums[i] != expected_num:
                return expected_num

    def missingNumber2(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

    def missingNumber3(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    def missingNumber4(self, nums):
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


if __name__ == '__main__':
    Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
