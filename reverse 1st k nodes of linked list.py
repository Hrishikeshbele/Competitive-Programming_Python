'''
Given a linked list A of length N and an integer B.

You need to reverse first  B nodes in the linked list A.
A = 1 -> 4 -> 6 -> 6 -> 4 -> 10
B = 2
 
Output:

 4 -> 1 -> 6 -> 6 -> 4 -> 10
 
 '''
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        temp=A
        p=A
        k=0
        while p and k<B:
            p=p.next
            k+=1
    
        curr=A
        prev=p
        k=0
        while curr and k<B:
            #print(curr,prev)
            a=curr.next
            curr.next=prev
            prev=curr
            k+=1
            if k<B:
                curr=a
            
        return curr
            
            
            
