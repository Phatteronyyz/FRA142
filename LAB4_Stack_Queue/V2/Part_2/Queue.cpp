#include <bits/stdc++.h>
#include "Queue.h"
using namespace std;

Queue :: Queue():LinkedList(){

}

Queue :: ~Queue(){
    
}

void Queue :: enqueue(int n){
    Node *newNode = new Node();
    newNode->setValue(n);
    insert(newNode,getSize());
}

Node *Queue :: dequeue(){
    Node *temp = tail;
    remove(0);
    return temp;
}

int Queue :: peek(){
    if(getSize()==0){
        cout << "Queue is empty" << endl;
        return 0;
    }
    else if(getSize()>0) return head->getValue();
}