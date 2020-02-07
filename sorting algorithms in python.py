#1. selection sort
def selectionsort(l):
    for i in range(len(l)):
        minval=i
        #finding index of min value in unsorted list and swapping it with first elm of unsorted list
        for j in range(i+1,len(l)):
            if l[j]<l[minval]:
                minval=j
                print(l[i],l[minval])
        #i is first elm of unsorted list, minval is index of min value in unsorted list 
        l[i],l[minval]=l[minval],l[i]
    return l
            
            
            
            
# 2. insertion sort 
def insertionsort(l):
    for i in range(len(l)):
        pos=i
        #iterating through all prev index 
        while pos>0 and l[pos]<l[pos-1]:
            print(pos)
            l[pos],l[pos-1]=l[pos-1],l[pos]
            pos=pos-1
    return l
