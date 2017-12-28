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


# https://leetcode.com/problems/fizz-buzz/description/
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [0] * n
        for i in range(1, n + 1):
            if i % 15 == 0:
                res[i - 1] = 'FizzBuzz'
            elif i % 3 == 0:
                res[i - 1] = 'Fizz'
            elif i % 5 == 0:
                res[i - 1] = 'Buzz'
            else:
                res[i - 1] = str(i)
        return res


if __name__ == '__main__':
    print(Solution().isValid('()[]{}'))
    print(Solution().isValid('([)]'))
