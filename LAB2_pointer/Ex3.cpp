#include <bits/stdc++.h>
using namespace std;

void callByValue(int var){
    var = 100;
}
void callByReference(int *var){
    *var = 200;
}

int main(){
    int var1 = 1;
    int var2 = 2;
    callByValue(var1);
    callByReference(&var2);
    
    cout << "var1 : " << var1 << endl;
    cout << "var2 : " << var2 << endl;
    return 0;
}