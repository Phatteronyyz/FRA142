#include <bits/stdc++.h>
#include "Stack.h"
using namespace std;

Stack :: Stack():linkedList(){

}

Stack :: ~Stack(){

}

void Stack :: push(Node *newNode){
    insert(newNode,0);
}

Node *Stack :: pop(){
    Node *temp = head;
    remove(0);
    return temp;
}

int Stack :: peek(){
    if(getSize()==0) cout << "Stack is empty" << endl;
    else return head->getValue();
}