'''
find next greater elm to left for all elms in list
ex.[1,3,2,4]
o/t: [-1, -1, 3, -1]

'''


def ngl(a):
    stack=[]
    ans=[]
    for i in range(0,len(a)):
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
        stack.append(a[i])
    return ans
