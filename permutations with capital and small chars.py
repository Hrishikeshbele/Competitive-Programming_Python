'''
given a string find its all combination with capital and small of each char in string.
 ex. ab
 output:'AB', 'Ab', 'aB', 'ab'
 
 idea: we use concept of recursion tree . each time we have decision to take small char or upper char. and we pass input string wo 1st char in next recursion.
                         
                         'ab'
                         /   \  (decision on a , wheter to take small or capital)
                        'a'  'A' 
                       / \    / \  (decision on b , wheter to take small or capital)
                    'ab''aB' 'Ab''AB' (ans)
                    
you can see in tree we are making input smaller and smaller at each level of tree by taking decision on its char and at last we will get empty string where we will get one elm of our ans.
                    
'''

def rec(s,ans,res):
    if not s:
        res.append(ans)
        return
    rec(s[1:],ans+s[0].upper(),res)
    rec(s[1:],ans+s[0],res)
    return res

print(rec('ab','',[]))
