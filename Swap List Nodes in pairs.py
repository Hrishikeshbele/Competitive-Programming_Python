'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.


idea is to use prev var node which points to head .we first store pointers of a(1st elm to be swapped), b(2nd elm to be swapped) and
c(elm used as pointer to next node after swap) then we assign a,b,c to theire corrsp position from prev and assing prev to a so that it
has val of a and pointer to c then in next iteration above process is iterated.
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        curr=A;
        while(curr is not None and curr.next is not None):
        #swapping curr and next values
            curr.val, curr.next.val = curr.next.val,curr.val 
        #incrementing elm to next to next elm
            curr=curr.next.next
         
        return A

    
#solution 2

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #dummy is assigned to prev and prev to empty node
        dummy=prev=ListNode(0)
        #pointing prev to head
        prev.next=head
        while prev.next and prev.next.next:
            a=prev.next
            b=prev.next.next
            c = prev.next.next.next
            prev.next=b
            prev.next.next=a
            prev.next.next.next = c
            #prev will have its val that of a and next pointer to c since we need pointer to next elm after these 2 elms
            prev=prev.next.next
        return dummy.next
            
