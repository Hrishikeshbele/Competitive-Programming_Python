'''
find the sum of digits of integer
'''

1.
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
    
    
 -> Even faster is the version without augmented assignments:
 
2.
def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r
