'''
given a array find the next greatest element of each element in array

ex.[1,3,4,2]

outpt: [3, 4, -1, -1]

we use the concept of stack. we transverse from back of array and keep one stack to store right elms.if current elm is less than last elm of stack we pop elms in stack until
we get elm greater than curr in stack and we append that elm to ans if we don't get any such elm we append -1 to ans. for whole approach see the youtube video of aditya verma.

'''
def ngr(a):
    stack=[]
    ans=[]
    for i in range(len(a)-1,-1,-1):
        if not stack:
            ans.append(-1)
        elif stack and stack[-1]>a[i]:
            ans.append(stack[-1])
        elif stack and stack[-1]<a[i]:
            while stack and stack[-1]<=a[i]:
                stack.pop()
            if stack:
                ans.append(stack[-1])
            elif not stack:
                ans.append(-1)
        stack.append(a[i]) # append curr elm to stack
    return ans[::-1]
