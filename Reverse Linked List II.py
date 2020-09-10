'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

idea here is to travel just upto 1 elm before m and then reverse the list between  m to n and then join pointer pointing to 1 elm before to head of reveresed list.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        
        for i in range(m-1):
            pre=pre.next
        # reversing list between m to n
        prev=None
        cur=pre.next #m node
        for i in range(n-m+1):
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        
        #joining next elm of n to pre
        pre.next.next=cur
        #joining pre to reversed list 
        pre.next=prev
        
        return dummy.next
        
        
