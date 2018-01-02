# coding: utf-8
# https://leetcode.com/problems/excel-sheet-column-number/description/
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(s):
            res *= 26
            res += ord(s[i]) - ord('A') + 1
            i += 1
        return res


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
