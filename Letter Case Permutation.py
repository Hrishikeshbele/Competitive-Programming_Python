'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

 

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

approach: 
let's see recursion tree for ex. a1b1. at each level we have choices based on which we get new strings.

                                   a1b1
								  /     \  (choice on a, whether to take small or capital a)
							    a       A
								|         | (choice on 1, note that we have only one choice on 1 i.e to take it )
							   a1      A1
							 /	  \    /   \  (choice on b)
						  a1b    a1B A1b   A1B
						   |      |   |    |   (choice on 1)
						a1b1    a1B1 A1b1 A1B1   (our ans)
            
'''


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def rec(s,ans,res):
            if not s:
                res.append(ans)
                return
            if s[0].isdigit():
                rec(s[1:],ans+s[0],res)
            elif s[0].isalpha():
                rec(s[1:],ans+s[0].upper(),res)
                rec(s[1:],ans+s[0],res)
            return res

        
        return rec(S.lower(),'',[])
        
