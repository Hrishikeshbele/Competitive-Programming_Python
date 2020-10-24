'''
Given an string. The task is to generate and print all of the possible subsequences of the given string .

ex.
Input : abc
Output : a, b, c, ab, bc, ac, abc

Approach: https://www.geeksforgeeks.org/generating-all-possible-subsequences-using-recursion/
For every element in the array, there are two choices, either to include it in the subsequence or not include it.Apply this for every element in the array starting 
from index 0 until we reach the last index. Print the subsequence once the last index is reached. 

'''
def ss(s,comb,ans): 
    if len(s)==0:
        ans.append(comb)
        return
    ss(s[1:],comb+s[0],ans) # adding curr char to our comb
    ss(s[1:],comb,ans) # not adding curr char to our comb
    return ans

