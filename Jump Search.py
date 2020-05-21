'''
The basic idea is to check fewer elements (than linear search) by jumping ahead by fixed steps or skipping some elements in place of searching all elements.

What is the optimal block size to be skipped?:
n the worst case, we have to do n/m jumps and if the last checked value is greater than the element to be searched for, we perform m-1 
comparisons more for linear search. Therefore the total number of comparisons in the worst case will be ((n/m) + m-1).value of the function
((n/m) + m-1) will be minimum when m = √n. Therefore, the best step size is m = √n.

'''

def jumpsearch(arr,x):
    step=int((len(arr))**0.5)
    for i in range(0,len(arr),step):
        if arr[i]==x:
            return(i)
        elif arr[i]>x:
            for j in range(i-step,i):
                if arr[j]==x:
                    return(j)
    return(-1)
