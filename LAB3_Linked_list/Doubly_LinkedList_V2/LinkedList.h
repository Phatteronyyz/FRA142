#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include "Node.h"
class linkedList
{
    private:
        int size = 0;

    public:
        Node *curr;
        Node *head;
        Node *tail;
        Node *temp;
        linkedList();
        void insert(Node *newNode, int pos);
        Node *remove(int pos);
        int getSize();
};
#endif