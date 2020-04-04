'''
Write a function that takes an unsigned integer and returns the number of 1 bits it has.
The 32-bit integer 11 has binary representation:
00000000000000000000000000001011
so the function should return 3.
'''
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count=0
        for i in bin(A)[2:]:
            if i=='1':
                count+=1
        return count
        
#another solution
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count=0
        while A>0:
            count+=int(A%2==1)
            A=A/2
        return count

    
 #bits solution
#remeber that A-1 will unset last set bit and unset following bits then by taking and we are clearing that following set bits
#so A&=A-1 will clear last set bit from repretn we count how many bits we cleared that is no of 1's in it's repretn
# Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000
def numSetBits(self, A):
        count = 0
        while A > 0:
            A =A&A - 1
            count += 1
        return count


        
