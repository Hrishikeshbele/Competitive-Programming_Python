'''
For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 
'''
'''
idea:
we iterate through a list of email addresses. for every email address, we first split it w.r.t '@' and store 
the first and second part differently then we take the first section of the first part after splitting it w.r.t '+'.
then we split that part w.r.t '.' and join them after that to remove '.' from the first section and we finally append 
this email to ans1. since we have to return unique emails we return len of the set of list.
'''

def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ans1=[]
        for email in emails:
            first,sec=email.split('@')
            ans=''.join(first.split('+')[0].split('.'))
            ans1.append(ans+'@'+sec)
            
        return len(set(ans1))
        
