'''
N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring, 
a switch also changes the state of all the bulbs to the right of current bulb. Given an initial state of all
bulbs, find the minimum number of switches you have to press to turn on all the bulbs. You can press the same switch multiple times.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, a):
        # Python program to find number switch presses to 
        n=len(a)
        count = 0

        res = 0
        for i in range(n): 
        # if the bulb's original state is on and count 
        # is even, it is currently on... 
        # no need to press this switch 
            if (a[i] == 1 and count % 2 == 0): 
                continue

        # If the bulb's original state is off and count 
        # is odd, it is currently on... 
        # no need to press this switch 
            elif(a[i] == 0 and count % 2 != 0): 
                continue

        # if the bulb's original state is on and count 
        # is odd, it is currently off... 
        # Press this switch to on the bulb and increase 
        # the count 
            elif (a[i] == 1 and count % 2 != 0): 
                res += 1
                count += 1

        # if the bulb's original state is off and 
        # count is even, it is currently off... 
        # press this switch to on the bulb and 
        # increase the count 
            elif (a[i] == 0 and count % 2 == 0): 
                res += 1
                count += 1
        return res 

