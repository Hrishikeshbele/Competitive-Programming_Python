'''
he gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]
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
        

