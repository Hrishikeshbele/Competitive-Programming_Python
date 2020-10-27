'''
Merge 2 sorted linked lists and return it as one sorted list.

'''

 #new iterative solution
#In solution we have a dummy head, and a tail indicating last node in this growing List. 
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
        


        
      
