#include <bits/stdc++.h>
#include "Stack.h"
#include "Queue.h"
using namespace std;

int main(){
    Stack st;
    Queue q;

    Node node1;
    Node node2;
    Node node3;
    Node node4;
    Node node5;
    node1.setValue(10);
    node2.setValue(20);
    node3.setValue(30);
    node4.setValue(40);
    node5.setValue(50);

    cout << "-------Stack-------" << endl;
    st.push(&node1);
    st.push(&node2);
    st.pop();
    st.push(&node4);
    cout << st.peek();
    cout << endl;

    cout << "-------Queue-------" << endl;
    q.enqueue(&node3);
    q.enqueue(&node5);
    cout << q.peek();


    return 0;
}