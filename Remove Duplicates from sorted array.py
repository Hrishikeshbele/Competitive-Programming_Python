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
	       
	            
