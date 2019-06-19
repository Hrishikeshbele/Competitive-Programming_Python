'''
You are given a string, S, and a list of words, L, that are all of the same length.
'''
#below is my earlier solution which was not passing all test case:
def findSubstring(A, B):
    key=sorted(''.join(B))
    key_sum=0
    ind=[]
    for ch in key:
        key_sum += ord(ch)
    for i in range(len(A)):
        ascii_sum = 0
        for ch in A[i:i+len(key)]:
            ascii_sum += ord(ch)
        if ascii_sum==key_sum and sorted(A[i:i+len(key)])==key :
            ind.append(i)
    return ind
    
    
   #2nd solution
   
   from collections import Counter
from collections import defaultdict
def findSubstring(A, B):
    c=Counter(B)
    m=len(B)
    n=len(B[0])
    ret=[]
    tot_len=m*n
    for k in range(n):
        left=k
        subd = defaultdict(int)
        count=0
        for j in range(k,len(A)-n+1,n):
            word=A[j:j+n]
            if word in c:
                subd[word]+=1
                count+=1
                while(subd[word]>c[word]):
                    subd[A[left:left+n]]-=1
                    left+=n
                    count-=1
                if count==m:
                    ret.append(left)
            else:
                left=j+n
                subd=defaultdict(int)
                count=0
    return ret
                    
    
    
