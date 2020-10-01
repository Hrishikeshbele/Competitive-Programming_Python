'''
given a array and element return the element in array whose diff with target elm is min.
ex.
a=[1,2,3,4,7]
target=5
here 4 have min diff with target elm 5. so we will return ans as 5. 
'''

def bs_min_diff(a,k):
    l,r=0,len(a)-1
    ans=0
    while l<=r:
        mid=(l+r)//2
        if a[mid]==k:
            return a[mid]
        elif a[mid]<k:
            l=mid+1
        else:
            r=mid-1
            
    if abs(a[l]-k) < abs(a[r]-k):
        return a[l]
    else:
        return a[r]
