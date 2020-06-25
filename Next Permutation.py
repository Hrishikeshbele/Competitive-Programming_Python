'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

idea: we start from 
'''


def nextpermutation(nums):
    #corner cases
    if len(nums)==1 or not nums:
        return 
    #getting last elm index to start backtracking with
    i=len(nums)-2

    while i>=0 and nums[i]>=nums[i+1]:
        i-=1
    
    if i != -1:
        j=i+1
        while j<(len(nums)) and nums[j]>nums[i]:
            j+=1
            
        
        j-=1
        nums[i],nums[j]=nums[j],nums[i]
    return nums[:i+1]+nums[i+1:][::-1]

nums=[1,3,2]
print(nextpermutation(nums))


    
