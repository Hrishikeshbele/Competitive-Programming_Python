'''
given a array and window size calculate the max sum of subarray having size k.

ex. [1,5,3,4,2]

output: 8 (sum of 5 and 3)

we use the concept of sliding window to solve the problem .first we traverse one pointer to k position and other at 0 postion then we move the window to right by substracting 
first elm and adding next elm.

'''
def fun(arr,k): 
    j=-1
    s=0
    i=0
    for z in range(k):
        j+=1
        s+=arr[z]
    while j<len(arr)-1 and i <j:
        s=max(s,s-arr[i]+arr[j+1])
        i+=1
        j+=1
        
        
    return s
