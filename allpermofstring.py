'''
given a string find all its permutations
'''
def perms(s):        
    if(len(s)==1): return [s]
    result=[]
    for i,v in enumerate(s):
        #for every char we add to it perm of remaing string expect that char 
        result += [v+p for p in perms(s[:i]+s[i+1:])]
        print(v,result)
    return result
