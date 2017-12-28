# https://leetcode.com/problems/valid-parentheses/description/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = '({['
        right = ')}]'
        test = []
        for i in s:
            if i in left:
                test.append(i)
            if i in right:
                if len(test) == 0:
                    return False
                if left.index(test.pop()) != right.index(i):
                    return False
        return len(test) == 0


# https://leetcode.com/problems/reverse-string/description/
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(i for i in reversed(s))


if __name__ == '__main__':
    print(Solution().isValid('()[]{}'))
    print(Solution().isValid('([)]'))
