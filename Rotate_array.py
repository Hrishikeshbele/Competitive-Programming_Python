'''
Given an unsorted array arr[] of size N, rotate it by D elements (clockwise).

ex. 1 2 3 4 5  when rotated by 2 elements, it becomes 3 4 5 1 2.
'''
#code
n=int(input())
for i in range(n):
    l,k=input().split()
    arr=input().split()
    new_arr=arr[int(k):]+arr[:int(k)]
    print(*new_arr)
