'''
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name 
(if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.
Example:
Input: "/a//b////c/d//././/.."
Output: "/a/b/c"

idea:Keep a stack tracking the directory level, skip over the . and only append directories which are not the . or .. When an .. is encountered pop from the stack 
(go up a level in the hierarchy) only if you have something in the stack, otherwise do nothing (empty stack encountering ..).

'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        for i in path.split('/'):
            if i not in ['.','','..']:
                stack.append(i)
                
            if i=='..' and stack:
                stack.pop()
        return '/'+'/'.join(stack)
