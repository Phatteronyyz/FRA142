#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,ans=1;
    cout << "Enter a number less than 100 : " ;
    cin >> n;
    cout << "Factorial of " << n << " = " ;
    for(int i = n;i>=1;i--){
        if(i==n) cout << i << " ";
        else cout << " x " << i ;
        ans*=i;
    }
    cout << " = " << ans;
  
    return 0;
}