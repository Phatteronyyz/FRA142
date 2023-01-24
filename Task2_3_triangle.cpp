#include <bits/stdc++.h>
using namespace std;
int main(){
    //ios::sync_with_stdio(0); cin.tie(0);
    int t,s;
    cout << "Please enter the type of triangle : ";
    cin >> t;
    cout << "Please enter the height of triangle : ";
    cin >> s;
    if(t==1){
        for(int i=0;i<s;i++){
            for(int j=0;j<s;j++){
                if(i<=(j-1)) cout << " ";
                else cout << "*";
            }
            cout << "\n";
        }
        for(int i=0;i<s-1;i++){
            for(int j=0;j<s-1;j++){
                if(j<=(s-i-2)) cout << "*";
            }
            cout << "\n";
        }
    }
    if(t==2){
        for(int i=0;i<s;i++){
            for(int j=0;j<(s*2)-1;j++){
                if((j<s-i-1) or (j>s+i-1)) cout << " ";
                else cout << "*";
            }
            cout << "\n";
        }
    }
    if(t==3){
        for(int i=0;i<s;i++){
            for(int j=0;j<s;j++){
                if(j<=(s-i-2)) cout << " ";
                else cout << "*";
            }
            cout << "\n";
        }
        for(int i=0;i<s;i++){
            for(int j=0;j<s;j++){
                if(i<=(j)) cout << "*";
                else cout << " ";
            }
            cout << "\n";
        }
    }
    
    return 0;
}