#include <bits/stdc++.h>
using namespace std;
int main(){
    //ios::sync_with_stdio(0); cin.tie(0);
    double a,t;
    char c;
    cout << "Please enter temperature : ";
    cin >> a >> c;
    if(c == 'K'){
        cout << a << " " << c << " = ";
        cout << a-273.15 << " " << 'C' << " = ";
        cout << 1.8*a-459.69 << " " << 'F';
    }
    else if(c == 'F'){
        cout << a << " " << c << " = ";
        cout << (0.5556)*(a-32) << " " << 'C' << " = ";
        cout << (a+459.69)/1.8 << " " << 'K';
    } 
    else if(c == 'C'){
        cout << a << " " << c << " = ";
        cout << a+273.15 << " " << 'K' << " = ";
        cout << ((9/5)*a)+32 << " " << 'F';
    } 
  
    return 0;
}