'''
basic operation with linked list
'''
#finding lenght of linked list
def lenofll(head)
  len=0
  while head:
      len+=1
      head=head.next
  return len
#finding middle of linked list using 2 pointer technique
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #return slow:- slow points to mid elm in odd len case or first elm of second half in even len case.
         
