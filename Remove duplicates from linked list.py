'''
if linked list has more than duplicate values remove all except one duplicate values.

ex. 
Input: 1->2->3->3->4->4->5
Output: 1->2->3->4->5

idea : we transverse the list normally and when we incounter a repeated elm we move forward until we find elm which is not duplicate and then we assing this elm as next of stored 
pointer to first duplicate elm .

'''
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        t=head
        while head and head.next:
            prev=head
            if head.val==head.next.val:
                while head.next and  head.val==head.next.val:
                    head=head.next
                head=head.next
                prev.next=head
            else:
                head=head.next
            
        return t
