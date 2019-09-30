'''
Navi is a counter strike pro. He always say how good he is at counter strike. After being tired of Navi, his friends decided to test his skills at shooting. 
They put M targets on a  x-y plane, each target is denoted by (X, Y) where X is x-coordinate and Y is y-coordinate. 
His friends also gave him N locations on  plane from where Navi can shoot the targets. Navi knows that he can shoot a target if Manhattan distance between his location and target is ≤ D. 
If Navi can shoot more than half of the targets (for odd values of M check only for the integral part of half of M, say , ) only then his friends believe that he is a pro at counter strike otherwise he is not.

SAMPLE INPUT 
1
3 3 5
1 1
2 2
3 3
1 0
0 0
2 0
SAMPLE OUTPUT 
YES
Explanation
First location is at 1,1 , we can shot any of the given targets from here so count> 3/2, therefore YES.
'''
#first we store the the values on location and target in different arrays then we calculate manhattan distance between each position and 
# and target value's if distance is <d we increase the count. if count> target arr length/2 we print yes.


import math
# Write your code here
    
def solution():
    test= int(input())  
    for i in range(test):
        n,m,d=map(int,input().split())
        cord=[]
        for j in range(n):
            x,y=map(int,input().split())
            cord.append([x,y])
        target=[]
        for j in range(m):
            x,y=map(int,input().split())
            target.append([x,y])
        targetlen=len(target)
        count=0;
        for j in range(n):
            x,y=cord[j]
            for z in range(m):
                p,q=target[z]
                if(abs(p-x)+abs(q-y)<=d):
                    count+=1;
                    break;
        if(count>=math.floor(targetlen/2)):
            print("YES")
        else: 
            print("NO")
          
if __name__ =="__main__":
    solution()
