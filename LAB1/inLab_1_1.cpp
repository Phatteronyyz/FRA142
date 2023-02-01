#include <bits/stdc++.h>
using namespace std;
int main(){
    int i;
    float a,ans=0;
    cin >> a;
    ans += a;
    for(i=2;i<=30;i++){
        if(i==15){
            continue;
        }
        else{
            switch (i%2){
                case 0:
                    a = a*1.2;
                    ans += a;
                    break;
                case 1:
                    a = a*0.8;
                    ans += a;
                    break;
                default:
                    continue;
            }
       } 
    }
    cout << ans;
    return 0;
}