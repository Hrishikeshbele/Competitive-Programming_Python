'''
given a array and element return the element in array whose diff with target elm is min.
ex.
a=[1,2,3,4,7]
target=5
here 4 have min diff with target elm 5. so we will return ans as 5. 

here will try to find target elm in array if not present will do binary search until condition satisfies and then at last we will get pointers pointing to 2 negbours of target elms 
whose diff will be min w.r.t target elm. from these  2 elms we will find elm whose diff is min and return it.
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
