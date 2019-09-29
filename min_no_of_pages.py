'''
 being the genius Mathematician Little Jhool is, he remembered that solving Mathematics problem given to him by his teacher was his favorite memory.

He had two types of notebooks, when he was a kid.

 problems could be solved in one page, in the first notebook.
 problems could be solved in one page, in the second notebook.
Little Jhool remembered how in order to maintain symmetry, if he was given with n problems in total to solve, he tore out pages from both notebooks, so no space was wasted. EVER!

But, now he's unable to solve his own problem because of his depression, and for the exercise of the week, he has to answer the queries asked by his psychologist.

Given n number of questions, print the minimum number of pages he needs to tear out from the combination of both the notebooks, so that no space is wasted.
print the minimum number of pages Little Jhool needs to tear out from the combination of both the notebooks. If it is NOT possible, print "-1".
ex.
2(n)
23
32
SAMPLE OUTPUT 
-1
3
Explanation
For : 2 pages from the 1 notebook, where  can be solved; 1 page from the 2nd notebook.

'''


n=int(input())
for i in range(n):
    np=int(input())
    x=np//10
    #we are using minm var so that we can find pair (i,j) whose sum is min.we assign value greater than x initial value to it.
    minm=x+2
    #then we try to find i,j such that their sum is np and store their sum in minm var.if we find new pair whose value is less than minm
    # we replace minm with new value
    for i in range(x+1):
        for j in range(x+1):
            if i*10+j*12==np:
                #to get min i and j
                if i+j <minm:
                    minm=i+j
    #if minm value does not change then it mean that we don't find any i,j pair whose sum is np, in this case return -1 else return minm value
    if minm==x+2:
        print(-1)
    else:
        print(minm)
    
