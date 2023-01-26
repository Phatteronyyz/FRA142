#include <bits/stdc++.h>
using namespace std;
int main(){
    int i;
    float a,ans=0;
    cin >> a;
    ans += a;
    for(i=2;i<=30;i++){
        if(i%2==0){
            a = a*1.2;
            ans += a;
        }
        else if(i==15){
            continue;
        }
        else if(i%2!=0){
            a = a*0.8;
            ans += a;
        }
    }

    cout << ans;
    return 0;
}