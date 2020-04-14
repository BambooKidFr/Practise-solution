# https://leetcode.com/problems/add-two-numbers/
# You are given two linked list representing two non-negative numbers
# The digits are stored in reverse order and
# each of these nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNpubers(self, l1, l2):
        """

        :type l1: ListNode
        :type l2: ListNode
        :rtype:  ListNode
        """
        prev = result = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev = prev.next
            carry //= 10
        return result.next
ListNode()
p=Solution()
p.addTwoNpubers(342,465)