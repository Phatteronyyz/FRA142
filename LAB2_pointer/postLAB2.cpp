#include <bits/stdc++.h>
using namespace std;

void cpy(int *idxa, int * idxb, int len){
    for(int i=0;i<len;i++){
        cout << (idxa+i) << " " << (idxb+i) << endl;
        *(idxb+i) = *(idxa+i);
    }
}

int main(){
    int arr[] = {1,2,3};
    int arr2[] = {};
    cpy(&arr[0],&arr2[0],3);
    int i;
    cout << endl;
    for(i=0;i<3;i++){
        cout << arr2[i];
    }
  
    return 0;
}
