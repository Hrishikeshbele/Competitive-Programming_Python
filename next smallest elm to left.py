'''
given the list find next smallest elm to left for all elm in list.
ex.a=[1,3,2,4]
o/t:[-1, 1, 1, 2]

'''
def nsl(a):
    ans=[]
    stack=[]
    for i in range(len(a)):
        if not stack:
            ans.append(-1)
        elif stack[-1]<a[i]:
            ans.append(stack[-1])
        elif stack[-1]>a[i]:
            while stack and stack[-1]>=a[i]:
                stack.pop()
            if stack:
                ans.append(stack[-1])
            elif not stack:
                ans.append(-1)
        stack.append(a[i])
    return ans
