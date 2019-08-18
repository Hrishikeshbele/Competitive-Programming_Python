'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
'''
#here idea is instead of pushing elm directly into stack we add second elm with it which will keep track of min elm in stack
# (x,minelm) :> stack[elm][minelm]
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data=[(None, float('inf'))]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #we keep track of min elm each time we add new elem and store it with new elm
        self.data.append((x,min(x,self.data[-1][1])))
        

    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            self.data.pop()
        

    def top(self):
        """
        :rtype: int
        """
        #return last elm x
        return self.data[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        #min elm will be second elm in last added entry
        return self.data[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#second solution using 2 stacks

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
