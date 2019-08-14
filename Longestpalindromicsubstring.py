'''
Given a string S, find the longest palindromic substring in S.

Input : "aaaabaaa"
Output : "aaabaaa"
'''
#If substring s[i+1..j-1] is a palindrome, then string s[i..j] is palindrome if and only if s[i] = s[j].
def longestPalindrome(s):
    M=[[False]*len(s) for i in range(len(s))]
    # if length of string is 1.since all substring of len 1 will be palindromic
    maxl=1
    start=0
    for i in range(len(s)):
        M[i][i]=True
    #for len==2.string of len 2 will be pelindromic if first and second char are equal
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            M[i][i+1]=True
            start=i
            maxl=2
    #for len>2
    #To calculate table[i][j],if the value of table[i+1][j-1] and str[i] is same as str[j] then we make table[i][j] true
    #k is len of substring
    for k in range(3,len(s)+1):
        #i is starting index of string,i can be for 0th char to 
        # (len(s)-k+1) char to make string of len k.
        for i in range(len(s)-k+1):
            #index of last char of string 
            j=i+k-1
            print(s[i:j+1])
            if (M[i+1][j-1] and s[i]==s[j]):
                M[i][j]=True
                if k>maxl:
                    start=i
                    maxl=k
    return s[start:start+maxl]
