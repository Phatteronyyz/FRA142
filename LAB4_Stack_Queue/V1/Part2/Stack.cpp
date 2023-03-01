#include<bits/stdc++.h>
#include "Stack.h"
using namespace std;

Stack::Stack():linkedList(){
    head = NULL;
    tail = NULL;
    curr = NULL;
    size = 0;
}

Stack::~Stack(){

}

void Stack::push(Node *newNode){
    curr = head;
    newNode->setNext(curr->getNext());
    curr->setNext(newNode);
    size += 1;
}

Node *Stack::pop(){
    curr = head;
    curr->setNext(curr->getNext()->getNext());
    curr = curr->getNext();
    curr->setNext(NULL);
    return curr;
}

void Stack::peek(){
    if(!size) cout << "Empty" << endl;
    else cout << head->getNext()->getValue() << endl;
}





