#include <bits/stdc++.h>
using namespace std;

void arraysum(int arr[],int size, int *ans){
    int *idx = NULL;
    for(int i = 0;i<size;i++){
        idx = &arr[i];
        *ans += *idx;
    }
}

int main(){
    int a[] = {1,2,3,4,5,6};
    int ans = 0;
    int n = size(a);
    arraysum(a,n,&ans);
    cout << ans;
  
    return 0;
}