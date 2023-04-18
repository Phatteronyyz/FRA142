#include <bits/stdc++.h>
using namespace std;
int main(){
    string s;
    vector<string> st;
    st.push_back("abc");
    getline(cin ,s);
    st.push_back(s);
    for(int i=0;i<st.size();i++){
        cout << st[i] << " ";
    }
  
    return 0;
}