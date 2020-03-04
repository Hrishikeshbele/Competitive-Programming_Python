'''
Given a list, return the value obtained after multiplying all numbers in a list.
'''
def multiply(x):
     prev=1
     for i in x:
         prev=prev*i
     return prev
