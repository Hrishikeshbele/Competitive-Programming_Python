'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
'''
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
	    #initialising curr variable to keep track of curr element
	    curr=A
	    while(curr.next is not None):
	        #if curr and next values are same we assign next to adress of next to next element
	        if curr.val == curr.next.val:
	            curr.next=curr.next.next
	        else:
	            #otherwise we simply increment curr to next value
	            curr=curr.next
	            
	    return A
	       
	            
# solution 2
# idea : we transverse the list normally and when we incounter a repeated elm we move forward until we find elm which is not duplicate and then we assing this elm as next of stored 
# pointer to first duplicate elm.

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first=head
        while head and head.next:
            #we check if curr val is equal to next node val if yes we assign
            #next of curr elm to next.next and continue if we found values at these nodes 
            #are same then we point next to next.next until two values are diff 
            if head.next.val==head.val:
                head.next=head.next.next
            #if 2 values are diff we assign this next node to curr head node
            else:
                head=head.next
        #return head of new ll
        return first

        
