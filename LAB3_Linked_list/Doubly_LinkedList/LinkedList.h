#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include "Node.h"
class linkedList
{
    private:
        int size = 0;
        
    protected:
        Node *tail;

    public:
        Node *curr;
        Node *head;
        linkedList();
        void insert(Node *newNode, int pos);
        Node *remove(int pos);
        int getSize();
        Node *gettail();

};
#endif