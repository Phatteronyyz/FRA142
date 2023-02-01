#include <bits/stdc++.h>
using namespace std;
tuple<int, int> swapAandB(int a, int b){
    return make_tuple(b,a); 
}
int main(){
    int a = 5, b = 3;
    tie(a,b) = swapAandB(a,b);
    cout << a << " " << b;
  
    return 0;
}