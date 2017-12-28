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


# https://leetcode.com/problems/happy-number/description/
class Solution(object):
    set1 = set()

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum1 = 0
        for s in list(str(n)):
            sum1 += (int(s)) ** 2
        if sum1 == 1:
            Solution.set1 = set()
            return True
        if sum1 in Solution.set1:
            Solution.set1 = set()
            return False
        Solution.set1.add(sum1)
        return self.isHappy(sum1)


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        list1 = []
        for number in range(2, n):
            end_pos = 0
            for i in list1:
                if number % i == 0:
                    break
            else:
                list1.append(number)
        return len(list1)

    def coutPrimes1(self, n):
        is_prime = [True] * n
        i = 2
        while i ** 2 < n:
            if is_prime[i]:
                j = i ** 2
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
        return max(sum(1 for i in is_prime if i is True) - 2, 0)

    def countPrimes2(self, n):
        not_prime = [False] * n
        count = 0
        i = 2
        while i < n:
            if not_prime[i] is False:
                count += 1
                j = 2
                while i * j < n:
                    not_prime[i * j] = True
                    j += 1
            i += 1
        return count


# https://leetcode.com/problems/roman-to-integer/description/
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        amap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        alist = []
        for i in s:
            alist.append(amap[i])
        res = 0
        i = len(alist) - 1
        maxnum = 0
        while i >= 0:
            if alist[i] >= maxnum:
                res += alist[i]
                maxnum = alist[i]
            else:
                res -= alist[i]
            i -= 1
        return res
