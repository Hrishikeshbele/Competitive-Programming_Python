'''
given a binary number and  k return binary string whose xor with given string is max whre  representing no of set bits in ans string.

approach: determine all values of ans with k bits set. and then take xor of it w.r.t all elm and return one who gave max int.

'''

import itertools 
def kbits(n,k):
    ans=[]
    for comb in itertools.combinations(range(n),k):
        s=['0']*n
        for c in comb:
            s[c]='1'
        ans.append(''.join(s))

    return ans

print(max(map(lambda x:int(x)^101,kbits(3,1))))
