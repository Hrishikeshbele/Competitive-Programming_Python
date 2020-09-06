'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

idea is to create 2 separate linked lists. one with nodes having values less than x and other having values greater than x and then merge them to get our final list. 

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1=l1=ListNode(0)  # head of the list with nodes values < x
        h2=l2=ListNode(0)  # head of the list with nodes values >= x
        # traverse the list and attach current node to l1 or l2 lists
        while head :
            if head.val<x:
                l1.next=head #assinging next of curr l1 pointer to curr head  
                l1=l1.next #pointing l1 pointer to next node 
            else:
                l2.next=head
                l2=l2.next #pointing l2 to next node
    
            head=head.next
        
        l2.next=None
        l1.next=h2.next
        
        return h1.next
        
        
        

