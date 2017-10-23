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


# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
class Solution(object):
    sum1 = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        self.convertBST(root.right)
        root.val += self.sum1
        self.sum1 = root.val
        self.convertBST(root.left)
        return root


# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return
        if head.next is None:
            return TreeNode(head.val)
        leng = self.getLength(head)
        mid_node = self.getNode(head, leng // 2)
        root = TreeNode(mid_node.val)
        self.setNode(head, leng // 2)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid_node.next)
        return root

    def getLength(self, head):
        ret = 0
        while head is not None:
            head = head.next
            ret += 1
        return ret

    def getNode(self, head, pos):
        target = 0
        while head is not None and target < pos:
            head = head.next
            target += 1
        return head

    def setNode(self, head, pos):
        target = 0
        temp = None
        while head is not None and target < pos:
            temp = head
            head = head.next
            target += 1
        if temp is not None:
            temp.next = None

    def sortedListToBST1(self, head):
        if head is None:
            return
        return self.toBST(head, None)

    def toBST(self, head, tail):
        slow = head
        fast = head
        if head == tail:
            return
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        thead = TreeNode(slow.val)
        thead.left = self.toBST(head, slow)
        thead.right = self.toBST(slow.next, tail)
        return thead
