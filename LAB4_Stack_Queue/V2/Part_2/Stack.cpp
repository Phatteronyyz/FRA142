#include <bits/stdc++.h>
#include "Stack.h"
using namespace std;

Stack :: Stack():LinkedList(){

}

Stack :: ~Stack(){
    
}

void Stack :: push(int n){
    Node *newNode = new Node();
    newNode->setValue(n);
    insert(newNode,0);
}

Node *Stack :: pop(){
    Node *temp = head;
    remove(0);
    return temp;
}

int Stack :: peek(){
    if(getSize()==0){
        cout << "Stack is empty" << endl;
        return 0;
    }
    else if(getSize()>0) return head->getValue();
}