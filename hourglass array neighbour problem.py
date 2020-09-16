'''
https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19

hourglass : 

a b c
  d
e f g
'''
# Complete the hourglassSum function below.
def hourglassSum(arr):
    ans=[]
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
            val=arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i][j]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]            
            ans.append(val)
    return max(ans)
