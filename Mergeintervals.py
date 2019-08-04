'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
'''
class Solution(object):
    def merge(self, interval):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #sorting interval by their first coordinate
        intervals = sorted(intervals, key=lambda interval:interval.start)
        result = []
        interval, l = intervals[0], len(intervals)
        
        for i in range(1, l):
            interval2 = intervals[i]
            #comparing start of next interval to end of curr interval
            if interval2.start > interval.end:
                result.append(interval)
                interval = interval2
            else:
                #finding end of curr interval from curr and next itervals
                interval.end = max(interval.end, interval2.end)
        
        result.append(interval)
        return result
            
