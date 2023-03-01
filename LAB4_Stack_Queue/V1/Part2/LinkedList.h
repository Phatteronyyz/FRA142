#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include "Node.h"
class linkedList
{
    private:
        int size;

    public:
        Node *curr;
        Node *head;
        Node *tail;
        linkedList();
        void insert(Node *newNode, int pos);
        Node *remove(int pos);
        int getSize();
        void printlist(linkedList ll);
        int peek();
};
#endif