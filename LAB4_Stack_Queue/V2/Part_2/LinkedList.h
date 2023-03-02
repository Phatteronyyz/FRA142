#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include "Node.h"
class LinkedList
{
    private:
        int size = 0;
        
    public:
        Node *tail;
        Node *curr;
        Node *head;
        LinkedList();
        void insert(Node *newNode, int pos);
        Node *remove(int pos);
        int getSize();

};
#endif