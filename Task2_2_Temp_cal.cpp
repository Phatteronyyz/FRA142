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
        t = a-273.15;
        cout << t << " " << 'C' << " = ";
        t = 1.8*a-459.69;
        cout << t << " " << 'F';
    }
    else if(c == 'F'){
        cout << a << " " << c << " = ";
        t = (0.5556)*(a-32);  
        cout << t << " " << 'C' << " = ";
        t = (a+459.69)/1.8;
        cout << t << " " << 'K';
    } 
    else if(c == 'C'){
        cout << a << " " << c << " = ";
        t = a+273.15;  
        cout << t << " " << 'K' << " = ";
        t = ((9/5)*a)+32;
        cout << t << " " << 'F';
    } 
  
    return 0;
}