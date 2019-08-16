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
