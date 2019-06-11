'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
'''


class MinStack:
    # @param x, an integer
    def __init__(self):
    #maintaining 2 stack one main stack and other to keep track of min in stack
        self.stack=[]
        self.minstack=[]
    def push(self, x):
        #if minstack is empty
        if not self.minstack :
            self.minstack.append(x)
            self.stack.append(x)
        else:
        #append min of x or minstack top
            self.minstack.append(min(x,self.minstack[-1]))
            self.stack.append(x)
        
    # @return nothing
    def pop(self):
        if self.stack:
            self.minstack.pop()
            self.stack.pop()


    # @return an integer
    def top(self):
        if not self.stack :
            return -1
        else:
            return (self.stack[-1])

    # @return an integer
    def getMin(self):
        if not self.minstack:
            return -1
        else:
            return (self.minstack[-1])
