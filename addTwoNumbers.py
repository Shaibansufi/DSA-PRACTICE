# LeetCode Problem: Add Two Numbers
# Problem Link: https://leetcode.com/problems/add-two-numbers/

# 2. Add Two Numbers
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = 0
        self.next = None


 
class Solution(object):
    def addTwoNumbers(self,l1,l2):
        dummy = ListNode(0)
        carry = 0
        current = dummy

        while l1 or l2 or carry :
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total//10
            current.next = ListNode(total%10)
            current = current.next

            if l1: l1 = l1.next 
            if l2: l2 = l2.next
        return dummy.next

