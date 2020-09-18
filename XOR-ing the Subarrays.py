'''
Problem Description

Given an integer array A of size N.

You need to find the value obtained by XOR-ing the contiguous subarrays, followed by XOR-ing the values thus obtained. Determine and return this value.

For example, if A = [3, 4, 5] :

Subarray    Operation   Result
3       None            3
4       None            4
5       None            5
3,4   3 XOR 4         7
4,5   4 XOR 5         1
3,4,5    3 XOR 4 XOR 5   2

Now we take the resultant values and XOR them together:

3 ⊕ 4 ⊕ 5 ⊕ 7 ⊕ 1⊕ 2 = 6 we will return 6.

'''

# solution 1 (brute force)
# idea is same as explained in problem description.

import functools 
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        #fn to cal xor of all elms of arr
        def helper(A):
            return functools.reduce(lambda x,y:x^y , A)
        temp=[]
        temp.extend(A)
        for i in range(2,len(A)):
            for j in range(len(A)-i+1):
                temp.append(helper(A[j:j+i]))
        temp.append(helper(A))
        return helper(temp)
       
       
 # solution 2 (optimized solution)
 
 '''
 Case 1 : Array length 3 (odd)

input is 
1 2 3

1^2^3^(1^2)^(2^3)^(1^2^3)

now count each digit
1 - 3 counts (zeroth position)
2 - 4 counts (first position)
3 - 3 counts    (second position)

so we can rewrite the above as

(1^1)^1^(2^2)^(2^2)^(3^3)^3  -> applying Rule 3
0^1^0^0^3 -> applying Rule 1
1^3 -> applying Rule 2
=> Result = 2
Notice that every even index (0, 2) occurs an odd number of times and that every odd index (1) occurs an even number of times.
So if the array length is odd then it is enough to XOR the 0,2,.... positions

Case 2 : Array length 4 (even)

input is 
4 5 7 3 (for easy understanding I am changing last 5 to 3)

4^5^7^3^(4^5)^(5^7)^(7^3)^(4^5^7)^(5^7^3)^(4^5^7^3)

4 - 4 counts
5 - 6 counts
7 - 6 counts
3 - 4 counts

since all the counts are even the result is 0.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # when len of arr is even
        if len(A)%2==0:
            return 0
        ans=0
        # if len of arr is odd
        for i in range(0,len(A),2):
            ans=(ans^A[i])
        return ans
