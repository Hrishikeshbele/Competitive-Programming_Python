'''
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements.
You need to find the minimum number of swaps required to sort the array in ascending order.

Sample Input 0

4
4 3 1 2
Sample Output 0

3
Explanation 0

Given array 
After swapping  we get 
After swapping  we get 
After swapping  we get 
So, we need a minimum of  swaps to sort the array in ascending order.

Explaination:
we will create 2 dictonaries. 1 whose keys will be index and values will be current elm at that index and 2nd will have elm values as key and its current position as value.
now we will loop through keys of 1st dict and if we find that key of curr elm is not equal to its value which means elm at that pos is not sorted. Loop through dictionary a
and whenever key doesn't match value use dictionary to find the current index of correct value.
Example 2:3, means index 2 has value 3. But it should actually hold 2 as value. So we use b[2], which gives us the current index of 2 in dictionary a.
b[2] gives us 4. Which means 2 is currently in index 4. So we swap index 2 and index 4 in dictionary a and increase the number of swaps count.
Then we update dictionary b accordingly. That is if 2:3 is swapped with 3:4 in dictionary a, we will swap 3:2 with 4:3
'''

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    pos={}
    val={}
    ans=0
    for i in range(len(arr)):
        pos[i+1]=arr[i]
        val[arr[i]]=i+1
    for i in pos:
        if pos[i]!=i:
            pos[val[i]],val[pos[i]]= pos[i],val[i]
            ans+=1
    return ans

    print(pos,val)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
