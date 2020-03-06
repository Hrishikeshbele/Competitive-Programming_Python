'''
link: https://projecteuler.net/problem=55
How many Lychrel numbers are there below ten-thousand?
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
We know from the problem statement that the maximum number of iterations for all numbers below 10,000 is <50 to form a Lychrel number.
'''

#function to reverse the number
def reverse(x):
    n=0
    while x>0:
        n=n*10+x%10
        x=x//10
    return n
    
#funtion to check if num is lychrel
def IsLychrel(num):
    for i in range(50):
        num+=reverse(num)
        if (num)==reverse(num):
            return False
    return True
        
#function to calculate no of lychrel numbers   
def nooflynchrel(n):
    ans=0
    for i in range(10,n):
        if IsLychrel(i):
            ans+=1
    return ans
#no of lychrel below ten-thousand
nooflynchrel(10000)
            
