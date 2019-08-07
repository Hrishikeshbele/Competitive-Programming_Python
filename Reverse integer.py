'''
Reverse digits of an integer.

Example1:

x = 123,

return 321
'''
class Solution:
	# @param A : integer
	# @return an integer
	def reverse(self, A):
        if(A > 0):
            k = int(''.join(reversed(str(A))))
            return k*(k < 2**31)
        else:
            k = -1*int(''.join(reversed(str(A)[1:])))
            return k * (k >-2 **31)
	     
	   
