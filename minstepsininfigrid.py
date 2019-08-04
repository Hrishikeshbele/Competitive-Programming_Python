'''
You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

'''
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, a, b):
        min = 0
        #since we can move in any direction min steps req to move from one point to 
        #another become max distance among their co-ordinates
        for i in range(1, len(a)):
            min += max(abs(a[i]-a[i-1]), abs(b[i]-b[i-1])) 
        return min
