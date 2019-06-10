'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''
class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, s):
        a=[]
        for i in s:
            if len(a)>0:
                if i==')' and a.pop()=='(':
                    continue
                if i==']' and a.pop()=='[':
                    continue
                if i=='}' and a.pop()=='{':
                    continue
            a.append(i)
        
        return int(len(a)==0)
            
        

