'''
given a sorted array find the floor of given elm. i.e element that is just smaller or equal to the target elm.

idea: we keep track of min element while doing binary search  which will eventually give us floor of target elm.

'''
def bs_floor_elm(a,k):
    l,r=0,len(a)-1
    ans=0
    while l<=r:
        mid=(l+r)//2
        if a[mid]==k:
            return a[mid]
        elif a[mid]<k:
            ans=a[mid]
            l=mid+1
        else:
            r=mid-1
    return ans
