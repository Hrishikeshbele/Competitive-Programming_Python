'''
Sort a linked list using insertion sort.
Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3
'''

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        head=A
        point=A
        #pointing given linked list to second elm
        A=A.next
        while A:
            #every time to  start with head of new linked list we assign point to head
            # at start of each iteration
            point=head
            while point != A:
                #iterate over linked list from head to point till it is sorted
                #if we value at point is greater than key value replace it o.w increament point
                if point.val>A.val:
                    point.val,A.val=A.val,point.val
                else:
                    point=point.next
            #increment A by one node
            A=A.next
        return head
