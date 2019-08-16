'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first=head
        #here we first find the len of linked list then mid of linked list
        #and we move the pointer to mid of linked list and return that pointer
        #see this pointer will always point to our desired elm since first it is pointed to first elm and then moving
        j=0
        while head:
            j+=1
            head=head.next
        head=first
        for i in range(j//2):
                head=head.next
        return head
  
  #another solution using pointer techique,we are moving slow pointer by one node and fast by 2 node and we see that 
  #by the point fast pointer reaches end of linked list our slow pointer reaches mid elm of linked list
  
  class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        
