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
