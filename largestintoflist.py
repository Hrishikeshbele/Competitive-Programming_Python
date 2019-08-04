'''
iven a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
'''

def largestNumber(self, A):
	    ''' When comparing numbers we must pick the one leading
	        to the best concatenated result:
	        787978 > 787879  so 7879 is 'bigger' than 78
	                    but     7879 is 'less' than 788
	    '''
	    
	    # Convert to string, for proper comparison a+b vs b+a
	    A = map(str, A)
      #here in cmp, x+y is compared lexagraphically(9>8>7) ex.95>59,330>303,9>23
	    res = ''.join(sorted(A, cmp= lambda a,b: cmp(a+b, b+a), reverse=True))
	    # Must left trim 0, apparently
	    res = res.lstrip('0')
	    return res if res else '0'
