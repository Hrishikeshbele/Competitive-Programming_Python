'''
given a string return all substrings of a given string 

Examples :

Input :  abcd
Output :  a 
          b
          c
          d
          ab
          bc
          cd
          abc
          bcd
          abcd
          
 we will solve this problem using recursion tree. see the video of aditya verma to get idea of full apprach.at each layer in tree we take decision regarding one char of string 
 whether to take it or not.
 '''
 
 def rec(s,ans,z):
    if not s:
        z.append(ans)
        return 
    # after taking decision for s[0] we remove it from string
    rec(s[1:],ans,z) # case where we are not adding curr elm to ans str
    rec(s[1:],ans+s[0],z) # we are adding curr elm to ans str
    return z
