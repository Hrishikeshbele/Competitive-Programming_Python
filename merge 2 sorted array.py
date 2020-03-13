'''
given two sorted array return the merged sorted array
solution approach: we initialise i,j which will act as pointer to indicate upto where elms are merged.we iterate over lists every time we 
compare 2 elements we append the smaller elm in result and increment pointer in that list. we continue this process until all elms of either
list exaust then we will add remaining elm of other list to result
'''

def mergearrays(a1,a2):
    i,j=0,0
    res=[]
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            res.append(a1[i])
            i+=1
        else:
            res.append(a2[j])
            j+=1
    return res+a1[i:]+a2[j:]
