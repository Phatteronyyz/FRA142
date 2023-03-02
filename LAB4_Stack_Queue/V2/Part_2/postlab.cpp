#include <bits/stdc++.h>
#include "Stack.h"
#include "Queue.h"
using namespace std;

int main(){
    Stack st;
    Queue r1,r2;

    int i;
    int a[] = {1,0,2,3,0,4,5};
    int b[] = {5,6,8,9,2,7,1};

    cout << "-------Post-Lab 1-------" << endl;

    for(i=0;i<size(a);i++){
        if(a[i]!=0){
            st.push(a[i]);            
        }
        else if(a[i]==0){
            int temp = st.peek();
            st.pop();
            st.push(0);
            st.push(temp);
        }
    }
    while(st.getSize()>0){
        cout << st.peek() << " ";
        st.pop();
    }
    cout << endl;

    cout << "-------Post-Lab 2-------" << endl;

    for(i=0;i<size(b);i++){
        if(b[i]%2==0){
            r1.enqueue(b[i]);
        }
        else if(b[i]%2!=0){
            r2.enqueue(b[i]);
        }
        if(r1.getSize()>0 and r2.getSize()>0){
            if(r1.peek()>r2.peek()){
                int temp = r1.peek();
                r1.dequeue();
                r1.enqueue(temp);
            }
            else if(r1.peek()<r2.peek()){
                int temp = r2.peek();
                r2.dequeue();
                r2.enqueue(temp);
            }
        }
    }
    cout << "row 2 : ";
    while(r1.getSize()>0){
        cout << r1.peek() << " ";
        r1.dequeue();
    }
    cout << endl;
    cout << "row 3 : ";
    while(r2.getSize()>0){
        cout << r2.peek() << " ";
        r2.dequeue();
    }

    return 0;
}