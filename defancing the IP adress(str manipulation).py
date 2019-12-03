'''
return a defanged version of that IP address.A defanged IP address replaces every period "." with "[.]".
'''

##solution1
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans=''
        for i in address:
            if i=='.':
                ans+='[.]'
            else:
                ans+=i
        return ans
       
##solution2         
def defangIPaddr(self, address):
        return '[.]'.join(address.split('.'))               


##solution3
def defangIPaddr(self, address):
        return address.replace('.', '[.]')

        
