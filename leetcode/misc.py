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


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        leftP = 0
        rightP = 0
        profit = 0
        while rightP < len(prices):
            while rightP < len(prices) - 1 and prices[rightP] < prices[rightP + 1]:
                rightP += 1
            else:
                profit += prices[rightP] - prices[leftP]
                leftP = rightP + 1
            rightP += 1
        return profit

    def maxProfit1(self, prices):
        profit = 0
        i = 1
        while i < len(prices):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]
            i += 1
        return profit
