'''
Write a program to find the node at which the intersection of two singly linked lists begins
'''
#Definition for singly-linked list.
#class node:
#    def __init__(self, x):
#        self.val = x
#       self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return: the head node in the linked list
    def getIntersectionNode(self, A, B):
        counta,countb=0,0
        heada,headb=A,B
        #find the length of A
        while A is not None:
            counta+=1
            A=A.next
        #find length of B
        while B is not None:
            countb+=1
            B=B.next
        #reassigning head node value to A,B because A,B now points to end of list
        A,B=heada,headb
        #if len of A is greater than B
        if counta>countb:
            for i in range(counta-countb):
                A=A.next
        #if len of B is greater than A
        else:
            for i in range(countb-counta):
                B=B.next
        #now since head of both list point at same distance from intersection we can iterate through both list elements
        while(A is not None or B is not None):
            if A == B:
                return A
            A=A.next
            B=B.next
        return None
            
        
        
            
        
    
