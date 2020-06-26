'''
write function to return k*k submatrices from matrix.

ex.
print out the  3x3 sub-boxes of the 9*9 grid .
m = [[1, 5, 9, 2, 4, 7],
     [0, 4, 6, 1, 5, 7],
     [6, 1, 8, 8, 6, 8],
     [4, 7, 3, 5, 7, 9],
     [8, 9, 6, 3, 1, 1],
     ]
Output: 
[[1, 5, 9]
[0, 4, 6]
[6, 1, 8],

[2, 4, 7]
[1, 5, 7]
[8, 6, 8],...]

idea here is increase the i,j by given k and then get k*k submatrix w.r.t that i,j then append it to ans.

'''


slice_x = 3
slice_y = 3
def submatrix(board,slice_x , slice_y):
    width=len(board[0])
    height=len(board)
    slices=[]
    for i in range(0,height,slice_x):
        for j in range(0,width,slice_y):
            slices.append([
                [board[a][b] for b in range(j,j+slice_x)]
                for a in range(i,i+slice_y)
            ])
    return slices
    
k=submatrix(board,slice_x , slice_y)
