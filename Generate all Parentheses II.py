'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.
 n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"

'''



class Solution:
	# @param A : integer
	# @return a list of strings
	def generateParenthesis(self, n):
	    #list to store pair of paratheses
        res = []
        #using stack and itialising stack with intial values of x,l,r
        #x-curr pair of pars,l-opening bracket,r-closing bracket
        s = [("(", 1, 0)]
        #run loop until stack is not empty
        while s:
            #assigning value to x,l,r every iteration
            x, l, r = s.pop()
            #if curr pair is not valid then moving to next pair
            if l - r < 0 or l > n or r > n:
                continue
            #when we reach to condition where l=r=n i.e no of closing 
            #and opening bracket are equal then that is valid str and append that to res
            if l == n and r == n:
                res.append(x)
            #for every pair add opening parth and increase l and wise-versa
            s.append((x+"(", l+1, r))
            s.append((x+")", l, r+1))
        #since we have to return sorted string
        return res[::-1]

#2nd elegent solution

class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        result = []
	#using helper function to find all pairs
        def helper(left, right, soFar):
	#left-no of opening parth,right-closing parth
	#unvalid conditions
            if left < 0 or right < 0 or left > right:
                return
	#no opening and closing bracket left
            if left == right == 0:
                result.append(soFar)
                return
	#adding opening parth and decreasing left count by 1 and vice-versa
            helper(left-1, right, soFar + '(')
            helper(left, right-1, soFar + ')')
        
        helper(A, A, '')
        return result


## recursion solution

'''
if no of opening bracket left is less than closing bracket left that means that we have use more opening bracket than closing and we will be able to use closing bracket.if left
opening and closing bracket are equal in number then parenthesis is balanced and when left opening parentheses are greater than closing parentheses string is not valid.

for n=2,                    '(' (o=1,c=2) # o denotes no of open bracket left to use , c denotes no of close bracket left to use
		            /  \
		  (0,2)	  '((' '()' (1,1)
		           |     | 
		  (0,1)	  '(()' '()(' (0,1) 
		            |     |
		  (0,0)	  '(())' '()()' (0,0)
		  
from the recursion tree we observe that if o is not equal to 0 we always have choice to add op bracket.when c>o we have choice to add clos bracket and when o=0 and c=0 we get result.
'''

def rec(c,o,ans,res):  # c : no of closing par , o: no of opning parth
    if c==0 and o==0:
        res.append(ans)
        return
    if o!=0:
        rec(c,o-1,ans+'(',res)
    if c>o:
        rec(c-1,o,ans+')',res)
    return res

print(rec(3,3,'',[]))
