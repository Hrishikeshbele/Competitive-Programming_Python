

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        last = None
        while A:
            #storing address of nxt elm of a to use later
            nxt = A.next
            #pointing next elm of a to last elm
            A.next = last
            #assign last as curr elm a
            last = A
            #moving forward a by one elm
            A = nxt
        #last will point to head of new linked list
        return last
            

