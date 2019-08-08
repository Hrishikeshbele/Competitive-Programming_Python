'''
given a sorted array and target elm find the position of given elm
'''
#iterative approach
def binarysearch(arr,target):
    start,end=0,len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if target==arr[mid]:
            return mid
        if target>arr[mid]:
            start=mid+1
        else:
            end=mid-1
    return False

#recursive approach
def binarysearch(arr,s,e,k):
    if s<=e:
        mid=e+s//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            return binarysearch(arr,s,mid-1,k)
        elif arr[mid]<k:
            return binarysearch(arr[mid+1:],mid+1,e,k)
    else:
        return -1
