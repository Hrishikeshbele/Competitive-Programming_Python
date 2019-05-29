'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
Example:
Given s = "Hello World",
return 5 as length("World") = 5.
'''
class Solution:
	# param A : string
	# return: an integer
	def lengthOfLastWord(self, A):
           #stip all white space at right side of string
	    A=A.rstrip()
	    if A:
                #first spliting the string by white space and then taking its last element
	        new=A.split(" ")[-1]
	        return len(new)
	    else:
	        return 0

