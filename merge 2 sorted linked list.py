'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20 
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20

idea is use 2 pointer and compare elm in 2 lists if elm in list1 is greater than elm in list2. we append that elm in sorted ll first.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        temp=ans=ListNode(0)
        while A and B:
            if A.val<B.val:
                ans.next=A
                ans=ans.next
                A=A.next
            elif A.val==B.val:
                ans.next=A
                ans=ans.next
                A=A.next
                ans.next=B
                ans=ans.next
                B=B.next
            else:
                ans.next=B
                ans=ans.next
                B=B.next
        # if only elements of A or B are remaining append remaining elm in one list if other has ended
        if A:
            ans.next=A
        if B:
            ans.next=B
        return temp.next
                
                
