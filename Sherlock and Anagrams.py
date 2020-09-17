'''
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen
Sample Input 0
2
abba
abcd

Sample Output 0
4
0

idea is to find all unique substring and sort them and see how many of them are equal.
'''

def sherlockAndAnagrams(s):
    ans=[]
    res=0

    for i in range(1,len(s)):
        d={}
        for j in range(len(s)-i+1):
            temp=''.join(sorted(s[j:j+i])) # all possible str of len 1,2,3... 
            ans.append(temp)
            if temp in d:
                d[temp]+=1
            else:
                d[temp]=1
            res+=d[temp]-1 # pair(n)=pair(n-1)+(n-1) ex. pair(3 item)=pair(2)+2
    return res
