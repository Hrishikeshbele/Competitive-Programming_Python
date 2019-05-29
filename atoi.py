'''
Implement atoi to convert a string to an integer.
Example :
Input : "-9 2704"
Output : -9
'''
class Solution:
    # param A : string
    # return: an integer
    def atoi(self, A):
       #striping white spaces in front size of string
        new=A.lstrip()
        signs=['-','+']
        ans=''
        lis=['0','1','2','3','4','5','6','7','8','9']
        #initialising sign variable to none type
        sign=None
        #spliting on white spaces and taking only first split
        if " " in new:
            new=new.split(' ')[0]
        #checking if first element of new string is some sign
        if new[0] in signs:
            sign=new[0]
        for i in range(len(new)):
            #for +34 or -7 cases
            if i==0 and sign:
                continue
            elif new[i] in lis:
                ans +=new[i]
            else:
                break
        if ans:
            #dealing with neg sign if present at starting at string
            if sign=='-' and sign:
                ans="-"+ans
            ans=int(ans)
            #dealing with overflow of int 
            if ans>=0:
                ans=min(ans,(2**31)-1)
            else:
                ans=max(-2**31,ans)
            return ans
        else:
            return 0
        
        
