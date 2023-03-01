#ifndef QUEUE_H
#define QUEUE_H

#include<bits/stdc++.h>
#include "LinkedList.h"
using namespace std;

class Queue: public linkedList{
    public:
    int size = 0;
        Queue();
        ~Queue();
        void enqueue(Node *newNode);
        Node *dequeue();
        void peek();
};
#endif