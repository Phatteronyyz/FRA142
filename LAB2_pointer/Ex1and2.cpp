#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int n = 10;
    cout << "Value of n : " << n << endl;
    cout << "Address of n : " << &n << endl;
    n = 5;
    cout << "Value of n after changed : " << n << endl;
    cout << "Address of n after changed : " << &n << endl;
    int *ptr = NULL;
    ptr = &n;
    *ptr = 3;
    cout << "Value of n after changed by poiter : " << n << endl;
    cout << "Address of n after changed by poiter : " << &n << endl;
  
    return 0;
}