'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Example :

Input : 

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3. 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        #initialising both pointer i,j to head A
        i,j=A,A
        while(j.next is not None and j.next.next is not None ):
            #incrementing pointer i by 1 and j by 2
            i=i.next
            j=j.next.next
            #if we found node such that i==j then we conclude there is cycle in linked list
            if i==j :
                break
        #if din't find anything return none
        if i != j:
            return None
        #setting one pointer slow to head of linked list and then incrementing it till we found node
        #such that both elem are equal which is starting point of linked list
        slow=A
        while(slow != j):
            j=j.next
            slow=slow.next
        return slow
        
  #second solution(to determine whether there is cycle in linked list)
  #we maintain 2 pointer. increment them every time by diff magnitude and check if they meet at some pt. if yes there is cycle
  def hasCycle(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False
            
            
            
        
        
         
         
        
