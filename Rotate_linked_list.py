'''

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

idea here is first find len of linked list and transverse to last element.then we assign next of last element to head to make linked list a cycle.
then transverse upto element from where you want cut the cycle and assign next to none.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        start=head
        #getting len of list
        len1=1
        while head.next:
            len1+=1
            head=head.next
        ## ElIf k is greater than the length of the list
        k=k%len1
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        head.next=start
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        tempnode=start
        for i in range(len1-k-1):
            tempnode=tempnode.next
        # Get the next node from the tempNode and then set the tempNode.next as None
        ans=tempnode.next
        tempnode.next=None
        
        return ans
            
            
        
