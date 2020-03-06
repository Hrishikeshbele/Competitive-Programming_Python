'''
reverse the given integer
'''
def reverse(n):
    ans=0
    while n>0:
        #n%10 will give you last digit of number which we are adding to our ans and *10 is insuring that they are placed in correct place(i.e 1's place,2's place)
        ans=ans*10+n%10
        #n//10 will remove last digit from number.since integer will remove stuff after decimal point
        n=n//10
    return ans
        
