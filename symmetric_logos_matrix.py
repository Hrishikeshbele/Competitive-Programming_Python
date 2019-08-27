'''
You are given a binary matrix of size N x N which represents the pixels of a logo.
1 indicates that the pixel is colored and 0 indicates no color.

For instance: Take a 5x5 matrix as follows:

01110
01010
10001
01010
01110

Observe that it is symmetric about both X-axis and Y-axis.
Output:
Print YES or NO in a new line for each test case
'''
#here idea is for logo to be symmetric each row and column of matrix should be pelidromic.


# Write your code here
#taking input from no of test cases 
for i in range(int(input())):
    n=input()
    matrix=[]
    #creating matrix of input data
    for i in range(int(n)):
        matrix+=[list(map(int,list(input())))]
    #taking transpose of given matrix
    trans1=list(zip(*matrix))
    for i,val in enumerate(trans1):
        trans1[i]=list(val)
    #checking if all rows are pelindrome
    for i in matrix:
        if i==i[::-1]:
            pass
        else:
            print('NO')
            break
    #cheking if all columns are pelindrome by checking rows of transposed matrix
    for j in trans1:
        if j==j[::-1]:
            pass
        else:
            print('NO')
            break
    else:
        print('YES')
   
    
