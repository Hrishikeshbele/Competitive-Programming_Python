'''
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
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
  
    # Print concatenation 
    # of all rows 
        for i in range(n): 
            ans+=arr[i]
        return ans
