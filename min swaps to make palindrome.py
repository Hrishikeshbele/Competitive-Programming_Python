'''
compute the number of times you need to swap to transform the string into a palindrome. By swap we mean reversing the order of 2 adjacent symbols. 
For example, the string "mamad" may be transformed into the palindrome "madam" with 3 swaps:
swap "ad" to get "mamda"
swap "md" to get "madma"
swap "ma" to get "madam"

solution approach:
1.we check if string can be converted into palindrome.
  >count the number of each letter in the input string a.If string length is even, all letters counts should be even.(ex.noon)
  b.If string length is odd, all letters counts should be odd except one.(ex.madam)
2.If the string length is odd, start by moving the element with odd count to the middle.
'''
