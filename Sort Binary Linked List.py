'''
Problem Description

Given a Linked List A consisting of N nodes.

The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.

You need to sort the linked list and return the new linked list.
Input 1:

 1 -> 0 -> 0 -> 1
 Output 1:

 0 -> 0 -> 1 -> 1
 
 idea is to create 2 linked list one having val 0 and other 1 while transversing list. and later we add second ll at end of 1st one.
 '''
 
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        head1=zero=ListNode(0)
        head2=one=ListNode(0)
        while A :
            if A.val==1:
                one.next=A
                one=one.next
            else:
                zero.next=A
                zero=zero.next
            A=A.next
        #pointing next of last elm of zero list to none
        one.next=None
        #attaching zero ll with one ll 
        zero.next=head2.next
        
        return head1.next
                
