'''
Reverse a linked list. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL,

return 5->4->3->2->1->NULL.
'''
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self,A):
        curr = A
        prev = None
        while (curr):
            #we are storing pointer to next node of curr node to move forward,since we have to set curr.next to prev elm pointer
            next=curr.next
            #setting next of curr elm to prev elm 
            curr.next=prev
            #storng curr elm as prev elm to use in next iteration
            prev=curr
            #moving foreward to next node
            curr=next
        head=prev
     
        return head
            
## more optimized solution

def reverseList(self,A):
    curr=A
    prev=None
    while curr:
        curr.next,prev,curr=prev,curr,curr.next

    return prev
            
