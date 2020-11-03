'''
there is n*n bingo grid containing characters 'o' or 'x' . determine it is considered to have bingo. it has bingo if either of following condition get satisfies:
 1. there is colm where every cell contain o
 2. there is row where every cell contains o
 3. there is diagonal where every cell contain o
 
 idea : here is to check if any row, column or either of 2 diagonal has all 'o' if yes return true else false.
 '''


def check_bingo(a):
    k=0
    l=len(a)
    #checking if any row having all 'o'
    for i in range(l):
        k=0
        for j in range(l):
            if a[i][j]=='o':
                k+=1
        if k==l:
            return 'Yes'
        print(k)
    #checking if any column having all 'o'
    k=0
    for j in range(l):
        k=0
        for i in range(len(a[0])):
            if a[i][j]=='o':
                k+=1
        if k==l:
            return 'Yes'

    #checking for left to right diagonal
    k=0
    for i in range(l):
        if a[i][i]=='o':
            k+=1
    if k==l:
            return 'Yes'


    #checking for right to left diagonal
    k=0
    for i in range(l):
        if a[i][l-1-i]=='o':
            k+=1
    if k==l:
            return 'Yes'
    return 'No'
    
a=[['o','o','o','o'],['o','x','o','o'],['o','x','o','o'],['o','x','o','o']]
print(check_bingo(a))
 
