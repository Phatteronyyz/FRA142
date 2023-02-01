#include <bits/stdc++.h>
using namespace std;
int main(){
    int num = 10;
    int *ptr;
    ptr = &num;
    cout << num << endl;
    cout << &num << endl;
    cout << ptr << endl;
    cout << &ptr << endl;
    cout << *ptr << endl;
    *ptr = 5;
    cout << "After changed value." << endl;
    cout << num << endl;
    cout << &num << endl;
    cout << ptr << endl;
    cout << &ptr << endl;
    cout << *ptr << endl;
    return 0;
}