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
            
        
        
        
   #second solution
'''
the idea is if you switch head, the possible difference between length would be countered. 
 On the second traversal, they either hit or miss. 
 if they meet, pa or pb would be the node we are looking for, 
 if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
'''

def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa,pb=headA,headB
         # if either pointer hits the end, switch head of that pointer and continue the traversal, 
          # if not hit the end, just move on to next
        while pa is not pb:
            pa= headB if pa is None else pa.next
            pb= headA if pb is None else pb.next
        # only 2 ways to get out of the loop, they meet or the both hit the end=None
        return pa
        
            
        
    
