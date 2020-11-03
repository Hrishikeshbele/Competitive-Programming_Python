/*
 there is n*n bingo grid containing characters 'o' or 'x' . determine it is considered to have bingo. it has bingo if either of following condition get satisfies:
 1. there is colm where every cell contain o
 2. there is row where every cell contains o
 3. there is diagonal where every cell contain o
 
 */
 
 #include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin>> n;
    vector<string> v(n);
    string s;
    for (int i=0 ; i<n; i++)
    {
        cin>>v[i];
    }
    cin>> v;
    for (int i=0; i<n;i++)
    {
        int k=0;
        for(int j=0;j<n;j++){
            if (v[i][j]=='o')
             k++;
        }
        if (k==n)
        {
            cout<<"Yes";
            return 0;
        }
    }
    for (int j=0;j<n;j++){
        int k=0;
        for(int i=0;i<n;i++){
            if (v[i][j]=='o' ) k++;
        }
        if (k==n){
            cout<<"Yes";
            return 0;
        }
    }
    int k1=0;
    for (int i=0 ;i<n;i++){
        if (v[i][n-1-i]=='o')k1++;

    }
    if( k1==n) {
        cout<<"Yes";
        return 0;
    }
    cout << "No";
    return 0;
    
}
