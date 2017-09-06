# https://leetcode.com/problems/min-stack/description/
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.alist = []
        self.min_pos = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.alist.append(x)
        if x < self.min:
            self.min = x
            self.min_pos.append(len(self.alist) - 1)
        elif len(self.min_pos) == 0:
            self.min = x
            self.min_pos.append(0)
        else:
            self.min_pos.append(self.min_pos[-1])

    def pop(self):
        """
        :rtype: void
        """
        self.alist.pop()
        self.min_pos.pop()
        if len(self.alist) != 0:
            self.min = self.alist[self.min_pos[-1]]
        else:
            self.min = None

    def top(self):
        """
        :rtype: int
        """
        return self.alist[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
