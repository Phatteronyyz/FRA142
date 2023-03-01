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
    remove(0);
}

int Stack :: peek(){
    return head->getValue();
}