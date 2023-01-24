#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int n=5;
    int i,j;
    for(i=0;i<(n*2)-1;i++){
        for(j=0;j<n;j++){
            if(i < 5 and j<=i) cout << "*";
            else if(i>=5 and j<=n-(i-n)-2) cout << "*";
            else cout << " ";
        }
        cout << "\n";
    }
  
    return 0;
}