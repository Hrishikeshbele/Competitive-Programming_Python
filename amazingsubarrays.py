'''
You are given a string S, and you have to find all the amazing substrings of S.

Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
Input
    ABEC

Output
    6

Explanation
	Amazing substrings of given string are :
	1. A
	2. AB
	3. ABE
	4. ABEC
	5. E
	6. EC
  '''
  #idea is simple just add the len of arr from position of vowel till last every time
  #solution1
  
  class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vo= "aeiouAEIOU"
        ans=0
        for i in range(0,len(A)):
            if A[i] in vo:
                ans=ans+(len(A)-i)
        return ans% 10003
  #solution2
  
  class Solution:
    # @param A : string
    # @return an integer
    def solve(self, a):
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ans=0
        for i,val in enumerate(a):
            if val in vowels:
                ans+=len(a[i:])
        return ans% 10003

                
