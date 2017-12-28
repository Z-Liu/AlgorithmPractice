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


if __name__ == '__main__':
    pass
