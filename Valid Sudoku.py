'''
** leetcode 36 **
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

here idea is simple first we check if all rows are valid then we check if all colums and submatrices are valid. if all are valid we return true else false.
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dicts={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        
        #checking if all rows are valid
        for i in (board):
            dicts={k:0 for k in dicts}
            for j in (i):
                if j != ".":
                    dicts[j]+=1
                    if dicts[j]>1:
                        return False
                    
        #checking if all columns are valid        
        for i in range(len(board)):
            dicts={k:0 for k in dicts}
            for j in range(len(board)):
                if board[j][i] != ".":
                    dicts[board[j][i]]+=1
                    if dicts[board[j][i]]>1:
                            return False
                        
        #checking if all submatrices are valid 
        for i in range(0,len(board),3):
            for s in range(0,len(board),3):
                dicts={k:0 for k in dicts}
                for j in range(i,i+3):
                    for k in range(s,s+3):
                        if board[j][k] != ".":
                            dicts[board[j][k]]+=1 
                            if dicts[board[j][k]]>1:
                                return False
                                                              
        return True
