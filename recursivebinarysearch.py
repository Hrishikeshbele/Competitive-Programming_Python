'''
given a sorted array and target elm find the position of given elm
'''
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
