'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5

idea here is to use pre linked list to store values of linked list without duplicates and head to traverse the linked list .when we find 2 consecutive values of list equal then we 
transverse to last value of equal values series and then point next of pre pointer to next of this last value. in this way to skip all duplicate values. 
'''

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #creating dummy node,pre and pointing it to head of linked list.
        dummy=pre=ListNode(0) #pointer pointing to last node of linked list without duplicates ##dummy node to keep pointer to head of linked list without uplicates 
        pre.next=head
        
        while head and head.next:
            #if 2 consecutive values are equal travel to last value of equal values series
            if head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head=head.next
                #move head pointer to value which is just next to equal values series
                head=head.next
                #point next of pre pointer to head. in this we skip the duplicates values.
                pre.next=head
              
            #if 2 consecutive elms are not equal
            else:
                #point pre pointer to next element of linked list 
                pre=pre.next
                # advance to next elm 
                head=head.next
                
        return dummy.next
