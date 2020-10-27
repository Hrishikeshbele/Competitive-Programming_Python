'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

idea: we start from back and find the i where decreasing sequence will start from i=1. then we find the elm at j which is next greater elm to elm at i and replace it with i and 
then we reverse the array from index i+1.
steps: 1. find decresing subarray sequence 2. replace elm just before found squence with next greatest elm in sequence 3. reverse this sequence after swapping
'''


def nextpermutation(nums):
    #corner cases
    if len(nums)==1 or not nums:
        return 
    #getting last elm index to start backtracking with
    i=len(nums)-2
    # finding i+1 from where decreasing sequence starts 
    while i>=0 and nums[i]>=nums[i+1]:
        i-=1
    # if we come out of while loop unnaturally then and the elm to be replaced with elm just outside decreasing sequence
    if i != -1:
        j=i+1
        while j<(len(nums)) and nums[j]>nums[i]:
            j+=1
        #substracting last unwanted increase in j 
        j-=1
        #exchanging elm at j and i indexes
        nums[i],nums[j]=nums[j],nums[i]
    return nums[:i+1]+nums[i+1:][::-1]




    
