#include <bits/stdc++.h>
using namespace std;
double a[10];
void getMAX(a[]){
    int mx = -1e9;
    for(int i=0;i<7;i++){
        mx = max(mx,a[i])
    }
    return mx;
}
void getMIN(a[]){
    int mn = 1e9;
    for(int i=0;i<7;i++){
        mn = mix(mn,a[i])
    }
    return mn;
}
void Avr(a[]){
    accumulate(a[0],a[6],sum)
    reruen sum/7;
}
int main(){
    for(int i=0;i<7;i++){
        cin >> a[i];
    }
    cout << getMAX(a);
    cout << getMIN(a);
    cout << Avr(a);
    
  
    return 0;
}