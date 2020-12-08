'''
Given an array of numbers, find GCD of the array elements.

'''

#include <iostream>
#include<bits/stdc++.h>
#define pb push_back
using namespace std;

int gcd(int a, int b){
    if(a==0)
        return b;
    return gcd(b%a,a);
    

}

int main() {
    int n;
    cin>>n;
    vector<int> a(n);
    
    for (int i=0;i<n;i++){
            cin>>a[i];
    } 
    int ans=a[0]
    for (int i=1;i<n;i++){
        ans=gcd(a[i],ans);
    }
    cout<<ans<<endl;
    return 0;
}


# python solution

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,b)

arr=[6, 90, 12, 18, 30, 18]
ans=arr[0]
for elm in arr:
    ans=gcd(elm,ans)
print(ans)
