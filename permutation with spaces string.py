'''
given string print all the possible permutations of string with spaces

ex. 'abc'
output: 'abc', 'ab-c', 'a-bc', 'a-b-c'

idea here is to use the recursion tree. at each node after first elm we have choice to include that elm with '_' or without it.
ex.   a
     / \
    ab a_b 
'''
def rec(s,ans,z):
    if not s:
        z.append(ans)
        return 
    # after taking decision for s[0] we remove it from string
    rec(s[1:],ans+s[0],z) # case where we are not adding curr elm to ans str
    rec(s[1:],ans+'-'+s[0],z) # we are adding curr elm to ans str
    return z

s='abc'
print(rec(s[1:],s[0],[]))
