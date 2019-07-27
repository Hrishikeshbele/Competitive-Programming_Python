'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast=slow=head
        #to find middle elm.elm from where palindrome will repeat
        #slow will point to first elm of second half of linked list
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        #reversing the half part
        prev=None  
        while slow:
            next=slow.next
            slow.next=prev
            prev=slow
            slow=next
        #comparing two half's elm by elm by it's value
        while(prev):
            if prev.val!=head.val:
                return False
            prev=prev.next
            head=head.next
        return True
        
        
