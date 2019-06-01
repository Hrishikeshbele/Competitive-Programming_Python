'''
just loved this technique called 2 pointers technique in which we maintain the two pointers and interate through sorted list
to find pair having some perticular sum.
ex.
arr=[10,20,35,50,55,75,80]
x=70
ispairsum(arr,x) return True.
'''
def ispairsum(arr,x):
    i=0
    j=len(arr)-1
    while(i<j):
        if (arr[i]+arr[j])==x:
            return True
            break
        elif (arr[i]+arr[j])>x:
            j-=1
        elif (arr[i]+arr[j])<x:
            i+=1
    return False
    
