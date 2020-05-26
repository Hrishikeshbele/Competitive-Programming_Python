'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

idea here is we will find len of linked list then transverse to index one less than elm we want to delete and we assign next of that node
to next.next to skip next elm.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size=0
        #store the pointer to head 
        start=head
        #find then lenght of ll
        while head:
            size+=1
            head=head.next
        # if lenght of list is equal to index of elm from last we want to delete then it is first elm that we want to delete so we return ll from next node to start
        if size == n :
            return start.next
        #reassign head to start of ll 
        head=start
        #interate to 1 less to elm index we want to delete
        for i in range(size-n-1):
            head=head.next
        #we point next of this node to next.next to skip elm we want to delete
        head.next=head.next.next
        
        return start
        
