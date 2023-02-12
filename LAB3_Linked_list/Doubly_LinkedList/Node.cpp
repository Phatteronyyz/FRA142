#include<bits/stdc++.h>
#include "Node.h"
using namespace std;

Node::Node(){
    value = 0;
    right = NULL;
    left = NULL;
}

Node::Node(int newValue, Node *newRight, Node *newLeft){
    value = newValue;
    right = newRight;
    left = newLeft;
}

void Node::print(){
    cout << value;
}

int Node::getValue(){
    return value;
}

void Node::setValue(int newValue){
    value = newValue;
}

Node* Node::getRight(){
    return right;
}

void Node::setNext(Node *newRight){
    next = newRight;
}

Node* Node::getLeft(){
    return left;
}

void Node::setNext(Node *newLeft){
    left = newLeft;
}