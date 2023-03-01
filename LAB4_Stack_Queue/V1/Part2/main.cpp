#include <bits/stdc++.h>
#include "stack.h"
#include "Queue.h"
using namespace std;

int main(){
    Stack st;
    Queue q;

    //setup
    Node stheadNode;
    Node sttailNode;
    st.head = &stheadNode;
    st.tail = &sttailNode;
    st.head->setNext(&sttailNode);
    sttailNode.setNext(NULL);
    //setup
    Node qheadNode;
    Node qtailNode;
    q.head = &qheadNode;
    q.tail = &qtailNode;
    q.head->setNext(&qtailNode);
    qtailNode.setNext(NULL);

    Node node1;
    Node node2;
    Node node3;
    Node node4;
    node1.setValue(10);
    node2.setValue(20);
    node3.setValue(30);
    node4.setValue(40);



    cout << "----Stack----" << endl;
    st.push(&node1);
    st.push(&node2);
    st.pop();
    st.peek();
    

    cout << "----Queue----" << endl;
    q.enqueue(&node3);
    q.enqueue(&node4);
    q.dequeue();
    q.peek();
    return 0;
}