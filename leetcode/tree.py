# coding: utf-8
from Queue import Queue


# https://leetcode.com/problems/merge-two-binary-trees/description/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    @staticmethod
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is not None and t2 is not None:
            rt = TreeNode(t1.val + t2.val)
            rt.left = Solution().mergeTrees(t1.left, t2.left)
            rt.right = Solution().mergeTrees(t1.right, t2.right)
            return rt
        elif t1 is not None:
            rt = TreeNode(t1.val)
            rt.left = Solution().mergeTrees(t1.left, None)
            rt.right = Solution().mergeTrees(t1.right, None)
            return rt
        elif t2 is not None:
            rt = TreeNode(t2.val)
            rt.left = Solution().mergeTrees(None, t2.left)
            rt.right = Solution().mergeTrees(None, t2.right)
            return rt

    def mergeTrees1(self, t1, t2):
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = Solution().mergeTrees1(t1.left, t2.left)
        t1.right = Solution().mergeTrees1(t1.right, t2.right)
        return t1

    def mergeTrees2(self, t1, t2):
        if t1 is None:
            return t2
        stack = []
        stack.append((t1, t2))
        while stack:
            t = stack.pop()
            if t[0] is None or t[1] is None:
                continue
            t[0].val += t[1].val
            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))
            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))
        return t1


# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        current_layer = []
        count = 0
        if root:
            current_layer.append(root)
        while True:
            next_layer = []
            if current_layer:
                count += 1
                for i in current_layer:
                    if i.left:
                        next_layer.append(i.left)
                    if i.right:
                        next_layer.append(i.right)
                current_layer = next_layer
            else:
                break
        return count


# https://leetcode.com/problems/invert-binary-tree/description/
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            if root.left:
                Solution().invertTree(root.left)
            if root.right:
                Solution().invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root

    def invertTree1(self, root):
        if root is None: return
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            current = queue.get()
            current.left, current.right = current.right, current.left
            if current.left:
                queue.put(current.left)
            if current.right:
                queue.put(current.right)
        return root
