#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int x=0 , y=0, i=-1;
    int a[] = {1, 2, 1, 3, 1, 2, 2, 1, 3, 2, 4, 1, 2, 3, 1, 4, 1, 2, 1, 3, 1, 2, 1, 1, 4};
    int n=size(a);
    while(i!=(n-1)){
        i ++;
        cout << x << " " << y << endl;
        if(a[i]==1) y++;
        else if(a[i]==2) x--;
        else if(a[i]==3) y--;
        else if(a[i]==4) x++;
        if(x==0 and y==0){
            x=1;
            y=1;
        }
    }
    cout << x << " " << y;
    
    return 0;
}