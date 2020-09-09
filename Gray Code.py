'''
he gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Approach:
For example, given n = 2, return [0,1,3,2]
For n=2: 00 01 11 10, Notice that the second half (11 and 10) are mirror of the first half (0 1) with additional 1 before it (10 11).
Now we have (00 01 11 10), in order to do n=3 we need to do the same. The 4 elements of n=2 will be our first half, to do the second half we mirror them to get (10 11 01 00) 
and add additional 1 before it (110 111 101 100). We get: For n=3: 000 001 011 010 110 111 101 100
'''

class Solution:
    # @param A : integer
    # @return a list of integers grayCode(int A)
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #when n = 2 , the gray code is [0,1,3,2] , equal to graycode(1)
        # + [reverse of graycode(1)](each element plus 2**(n-1))
        if n == 0:
            return [0]
        #calculating and storing graycode for n-1 
        temp = self.grayCode(n-1)
        #calculating half elm of graycode of n by reversing graycode(n-1)
        #and adding 2**(n-1) to it
        temp1 = [i+2**(n-1) for i in temp[::-1]]
        #storing the result as temp+temp1
        res = temp + temp1
        return res
        
## solution:2

def grayCode(A):
    res = [0]
    for i in range(A):
        #shifting bit by i to left
        t = 1<<i
        #adding t to each elm of reversed(res)
        temp = [j+t for j in reversed(res)]
        #adding temp to res
        res = res + temp
    return res    

## solution 3 (recursion)

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def helper(n):
            if n==0:
                return ['0']
            if n==1:
                return ['0','1']
            res=helper(n-1)
            return ['0'+i for i in res]+['1'+i for i in res[::-1]]
        
        return [int(j,2) for j in helper(n)]
