#include<bits/stdc++.h>
#include "Queue.h"
using namespace std;

Queue::Queue():linkedList(){
    head = NULL;
    tail = NULL;
    curr = NULL;
    size = 0;
}

Queue::~Queue(){

}

void Queue::enqueue(Node *newNode){
    curr = head;
    for(int i=0;i<size;i++){
        curr = curr->getNext();
    }
    newNode->setNext(tail);
    curr->setNext(newNode);
    size += 1;
}

Node *Queue::dequeue(){
    curr = head;
    curr->setNext(curr->getNext()->getNext());
    curr = curr->getNext();
    curr->setNext(NULL);
    return curr;
}

void Queue::peek(){
    if(!size) cout << "Empty" << endl;
    else cout << head->getNext()->getValue() << endl;
}





