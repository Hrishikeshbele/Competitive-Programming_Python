'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

>idea here is to use carry var to add values of each node corrsp same index in both ll and itself then take quetient and remainder of that carry to add values to our ans linked list
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #pointer var to store pointer to start of ans linked list
        ans=pointer=ListNode(0)
        carry=0
        #added carry in while loop condition to handle corner case of 1 same elm in both ll
        # ex [5],[5] ans would be [1,0]
        while l1 or l2 or carry:
            
            if l1:
                carry+=l1.val
                l1=l1.next
            
            if l2:
                carry+=l2.val
                l2=l2.next
            #for each iteration carry will add values of node at linkedlist 1 and 2 and                 # itself if not 0
            carry, remainder = divmod(carry, 10)
            ans.next=ListNode(remainder)
            ans=ans.next
           
        return pointer.next
            
        
