'''
given a number find the index of number if exist in fibonacci sequence else return -1.

Examples :

Input : 13
Output : 7

Input : 4
Output : -1

'''
#solution 1
def isfib(n):
    if n<2:
        return n
    a = 0
    b = 1
    c = 1
    res = 1
   
    # iterate until generated fibonacci number  
    # is less than given fibonacci number 
    while (c < n) : 
        c = a + b 
           
        # res keeps track of number of   
        # generated fibonacci number 
        res = res + 1
        a = b 
        b = c 
    if c==n:
        return res 
    else:
        return -1
        
#solutin 2

