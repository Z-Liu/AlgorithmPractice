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


# https://leetcode.com/problems/valid-anagram/description/
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in t:
            if i not in dict1:
                return False
            dict1[i] -= 1
        for i in dict1:
            if dict1[i] != 0:
                return False
        return True

    def isAnagram1(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(list(s)) == sorted(list(t))


# https://leetcode.com/problems/contains-duplicate/description/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return bool(len(nums) - len(set(nums)))


# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        for i in nums1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        dict2 = {}
        for i in nums2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        res = []
        for i in dict1:
            if i in dict2:
                res.extend([i] * min(dict1[i], dict2[i]))
        return res
