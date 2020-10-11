'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that 
the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container
contains the most water.
Note: You may not slant the container and n is at least 2.

the idea here is to use 2 pointers and move the left pointer and right pointer respectively to search for the next higher height.If height[L] < height[R],
move toward right(increment left pointer), else move left since Say height[0] < height[5],since area of (0, 4), (0, 3), (0, 2), (0, 1) will be smaller than 
(0, 5) since height will be equal to height[0] and lenth would const decrease, so no need to try them.           

'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start=0
        end=len(height)-1
        area=[]
        
        while start<end:
            if height[start]<=height[end]:
                #area = length * min (height_a, height_b), to maximize the area we want max both lenght and height
                area.append(min(height[end],height[start])*(end-start))
                start+=1   
                
            else:
                area.append(min(height[end],height[start])*(end-start))
                end-=1
                
            
                  
            
        return max(area)
            
            
