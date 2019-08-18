'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"()[]{}" is valid but "(]" and "([)]" are not.
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
            
#solution2

class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, l):
        op='({['
        cl=')}]'
        #we declare stack to store opening partheses and when last opening parth is same as curr closing parth pop the 
        #opening parth, in the end if stack is empty we colcluede that string is balanced 
        stack=[]
        for i in l:
            if i in op:
                stack.append(i)
            elif i in cl:
                #if closing parth but no opening parth for that so return false
                if len(stack)==0:
                    return int( False)
                elif i ==')' and stack.pop()=='(':
                    continue
                elif i =='}' and stack.pop()=='{':
                    continue
                elif i ==']' and stack.pop()=='[':
                    continue
                else:
                    return 0
        return int(len(stack)==0)
                
        

        

