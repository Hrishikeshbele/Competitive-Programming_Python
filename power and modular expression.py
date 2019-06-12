'''
1.Implement pow(A, B).
2.Implement pow(A, B) % C.
both in log(n) time
'''
def pow(a,b):
    if a==0:
        return 0
    if b==0:
        return 1
    if b%2==0:
        y=pow(a,b//2)
        return y*y
    else:
        return a*pow(a,b-1)
        
#modular expression calculation function      
 def mod(a,b,c):
    if a==0:
        return 0
    if b==0:
        return 1
    elif b%2==0:
        y=mod(a,b//2,c)
        return (y*y)%c
    else:
        return ((a%c)*mod(a,b-1,c))%c
