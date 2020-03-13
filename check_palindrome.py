'''
check if given string is pelindrome.
solution idea: iteratively check if last letter and first letter of string are equal if not then return false if yes check of substring
excluding first and last elm and basic condition is if len of str is less than 2 then it should be pelindrome so return true
'''

def ispalindrome(word):
    if len(word) < 2: 
        return True
    if word[0] != word[-1]: 
        return False
    return ispalindrome(word[1:-1])
    
