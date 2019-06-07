'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        curr=A;
        while(curr is not None and curr.next is not None):
        #swapping curr and next values
            curr.val, curr.next.val = curr.next.val,curr.val 
        #incrementing elm to next to next elm
            curr=curr.next.next
         
        return A
