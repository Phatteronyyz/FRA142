#ifndef STACK_H
#define STACK_H

#include<bits/stdc++.h>
#include "LinkedList.h"
using namespace std;

class Stack: public linkedList{
    public:
    int size = 0;
        Stack();
        ~Stack();
        void push(Node *newNode);
        Node *pop();
        void peek();
};
#endif