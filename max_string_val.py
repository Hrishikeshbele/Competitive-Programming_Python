'''
The little Monk loves to play with strings. One day he was going to a forest. On the way to the forest he saw a Big Tree(The magical tree of the forest). The magic of the tree was that, every leaf of the tree was in the format of string(having some value). Monk wants to have these type of leaves. But he can take only one. Help Monk to choose the most valuable leaf.

Format of the leaf:

a+b+c-d+c+d-x-y+x........, i.e. it contains a string holding a mathematical expression, and the value of that expression will be value of that particular leaf.
 
4+2-5+3+2-4
value: 2

'''
#no of input strings
n=int(input())
arr=[]
for j in range(n):
    str=input()
    sum=0
    sub=False
    #we are maintaining boolen var sub to check if '-' sign comes we set it to true value and substract that value and 
    #add all other numeric values.
    for i in str:
        if sub:
            sum -=int(i)
            sub=False
        elif i.isdigit():
            sum+=int(i)
        elif i=='-':
            sub=True
        elif i=='+':
            pass
    arr.append(sum)

print(max(arr))
