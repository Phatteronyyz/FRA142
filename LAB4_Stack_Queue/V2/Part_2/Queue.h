#ifndef QUEUE_H
#define QUEUE_H
#include "LinkedList.h"

class Queue : public linkedList{
    public :
        Queue();
        ~Queue();  
        void enqueue(Node *newNode);
        Node *dequeue();
        int peek();
};

#endif