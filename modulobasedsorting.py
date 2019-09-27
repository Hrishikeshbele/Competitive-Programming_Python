'''
Monk likes to experiment with algorithms. His one such experiment is using modulo in sorting.He describes an array modulo sorted as:
Given an integer k, we need to sort the values in the array according to their modulo with k. That is, if there are two integers a and b, and , then a would come before b in the sorted array. If  , then the integer which comes first in the given array remains first in the sorted array.
Given an initial array, you need to print modulo sorted array.
ex: 
12%6=0
18%6=0
17%6=5
65%6=5
46%6=4
So, the sorted order is: 12 18 46 17 65
'''
n,k=input().split()
arr=[int(x) for x in input().split()]
def func(mod):
    return mod % int(k)
# * will will print elm as 1 space separated elm. 
print(*sorted(arr, key = func))
