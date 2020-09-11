'''
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        def dfs(s,ind,path,res):
            #if we got 4 part of ip adress and s is empty we got one ip adress
            if ind==4:
                if not s:
                    res.append(path[:-1])
                return
            for i in range(1,4):
                # the digits we choose should no more than the length of s
                if i<=len(s):
                    #choose one digit
                    if i==1 :
                        dfs(s[i:],ind+1,path+s[:i]+'.',res)
                    #choose two digits, the first one should not be "0"
                    elif i==2 and s[0]!='0':
                        dfs(s[i:],ind+1,path+s[:i]+'.',res)
                    #choose three digits, the first one should not be "0", and should less than 256
                    elif i==3 and s[0]!='0' and int(s[:3])<=255:
                        dfs(s[i:],ind+1,path+s[:i]+'.',res)
        
        res=[]
        dfs(s,0,'',res)
        return res
        
                    
        
