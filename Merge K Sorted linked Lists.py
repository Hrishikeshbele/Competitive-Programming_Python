'''
Merge k sorted linked lists and return it as one sorted list.
idea is append all elm in heap first and then take min of them
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, lists):
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h) #only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next

        return dummy.next
            
 #new iterative solution
#In solution 2 we have a dummy head, and a tail indicating last node in this growing List. 
# At each step we append either l1 or l2 to tail, and update tail, l1 or l2 accordingly.

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #new to keep track of head of new linked list and tail to keep track of last node in growing link list
        new=tail=ListNode(None)
        while l1 and l2:
            if l1.val<=l2.val:
                tail.next=l1
                l1=l1.next
            else :
                tail.next=l2
                l2=l2.next
            #update tail
            tail=tail.next
        #to append remaining elm in one list if other becomes empty
        tail.next=l1 or l2
        #return head of new list
        return new.next
        


        
      
