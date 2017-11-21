# coding: utf-8
# https://leetcode.com/problems/single-number/description/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        adict = {}
        for i in nums:
            if i in adict:
                adict[i] += 1
            else:
                adict[i] = 1
        for i in adict:
            if adict[i] == 1:
                return i

    def singleNumber1(self, nums):
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    def singleNumber2(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber3(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a
