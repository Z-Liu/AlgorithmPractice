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
