# coding: utf-8
# https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            temp = head
            new_head = ListNode(temp.val)
            while temp.next:
                temp1 = new_head
                new_head = ListNode(temp.next.val)
                new_head.next = temp1
                temp = temp.next
        else:
            new_head = head
        return new_head

    def reverseList1(self, head):
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def reverseList2(self, head):
        if head == None or head.next == None:
            return head
        p = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return p


# https://leetcode.com/problems/merge-two-sorted-lists/description/
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        candidate1 = l1
        candidate2 = l2
        if candidate1:
            if candidate2:
                if candidate1.val < candidate2.val:
                    ret = candidate1
                else:
                    ret = candidate2
            else:
                ret = candidate1
        else:
            ret = candidate2
        new_curr = ListNode(None)
        while candidate1 and candidate2:
            if candidate1.val < candidate2.val:
                new_curr.next = candidate1
                new_curr = new_curr.next
                candidate1 = candidate1.next
            else:
                new_curr.next = candidate2
                new_curr = new_curr.next
                candidate2 = candidate2.next
        while candidate1:
            new_curr.next = candidate1
            new_curr = new_curr.next
            candidate1 = candidate1.next
        while candidate2:
            new_curr.next = candidate2
            new_curr = new_curr.next
            candidate2 = candidate2.next
        return ret
