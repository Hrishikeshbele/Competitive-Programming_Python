'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
 '''
 
import operator
class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        #maintaing stack for performing mathematical operations and 
        #storing results and int values
        ans=[]
        #dict to turn string operator into mathematical operator
        ops = { "+": operator.add, "-": operator.sub ,'*' : operator.mul,'/' : operator.truediv}
        for num in A:
            #if we found operator then take out last 2 elm and perform
            #operation of them and store value in as
            if num in ["/", "+","-", "*"]:
                a=ans.pop()
                b=ans.pop()
                ans.append(ops[num](b,a))
            else:
                #store int's in stack
                ans.append(int(num))
        return int(ans[-1])
                
#solution2
#everytime when operator comes we are poping last 2 elms and performing optn on them and storing result in stack.lastly return last elm of stack.
class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        s=[]
        op=['+', '-', '*', '/']
        for i in A:
            if i not in op:
                s.append(int(i))
            elif i=='/':
                num1 = s.pop()
                num2 = s.pop()
                s+=[num2/num1]
            elif i=='*':
                num1 = s.pop()
                num2 = s.pop()
                s+=[num2*num1]
            elif i=='+':
                num1 = s.pop()
                num2 = s.pop()
                s+=[num2+num1]
            elif i=='-':
                num1 = s.pop()
                num2 = s.pop()
                s+=[num2-num1]
        return int(s[-1])
        
        
                
            
        
