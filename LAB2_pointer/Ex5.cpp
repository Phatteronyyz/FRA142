#include <bits/stdc++.h>
using namespace std;
void swapAandB(int *a, int *b){
    int temp;
    temp = *b;
    *b = *a;
    *a = temp;
}
int main(){
    int a = 5, b = 3;
    swapAandB(&a,&b);
    cout << a << " " << b;    
  
    return 0;
}