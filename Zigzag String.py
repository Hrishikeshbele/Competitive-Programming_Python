'''
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"

idea: we keep on adding character to their respective row string while we transverse through string.we use index var to keep track of the row to which curr char belong and
step is used to adjust index such that curr char is get added to corrent row level string. as we reach at last row we decrease index and vice-versa.
'''
class Solution:
    # param A : string
    # param B : integer
    # return: a strings
    def convert(self, str, n):
        ans=""
    # special Case (Only one row) 
        if n == 1:
            return str
  
    # Creating  an array of strings for  n rows 
        arr=["" for x in range(n)] 
        row = 0
  
        for i in range(len(str) ): 
          

            arr[row] += str[i] 
  
        # If last row is reached,  
        # change direction to 'up' 
            if row == n - 1: 
                down = False
  
        # If 1st row is reached, 
        # change direction to 'down' 
            elif row == 0: 
                down = True
  
        # If direction is down,  
        # increment, else decrement 
            if down:
                row += 1
            else:
                row -= 1
                
  #second solution

def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
  
    # Print concatenation 
    # of all rows 
        for i in range(n): 
            ans+=arr[i]
        return ans
