'''
Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index
in the original list. Look at the sample case for clarification.
Input : [cat ,dog ,god, tca]
Output : [[1, 4], [2, 3]]
'''
class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self,A):
	    
    # hashmap with sorted string as key and list of anagrams as values
        hashmap = {}
    
        for index,word in enumerate(A):
        
        # sorted() returns a list, hence first convert it to a string 
        # so that we can use it as a key in the hashmap
            sorted_word = ''.join(sorted(word))
        
            if sorted_word not in hashmap:
            
            # create key if not present and associate 
            # the current word with it
                hashmap[sorted_word] = [index + 1]
            else:
            
            # append the current word to the list associated with the key
                hashmap[sorted_word] += [index + 1]
    
    # hashmap.values() returns a dict_values object in python 3, 
    # hence convert it into a list while returning        
        return list(hashmap.values())
        
        
 #2nd method
 
 class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, string):
        anagram_hash = {}
        #starting with index 1
        for index, animal in enumerate(string, 1):
            #initialising ascii sum to 0
            
            ascii_sum = 0
            #summing up ord of all char and storing in ascii_sum
            for ch in animal:
                ascii_sum += ord(ch)
                anagram_hash[ascii_sum] = [index]
            #checking if there any str in dict whose sum=curr ascii_sum if found we add curr index to its value list
            if anagram_hash.get(ascii_sum) != None:
                anagram_hash[ascii_sum].append(index)
            else:
            #else we add that elm to dict with its value as curr index
                anagram_hash[ascii_sum] = [index]
        #we return values of dict 
        return anagram_hash.values()
        
       
