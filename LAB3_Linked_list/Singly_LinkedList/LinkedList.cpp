#include <bits/stdc++.h>
#include "linkedList.h"
using namespace std;

linkedList::linkedList()
{
    head = NULL;
    tail = NULL;
    curr = NULL;
    size = 0;
}
int linkedList::getSize()
{
    return size;
}

void linkedList::insert(Node *newNode, int pos)
{
    if(pos <= ++size){
        if (pos == 0)
        {
            curr = newNode;
            newNode->setNext(head);
            head = curr;
            size++;
        }
        else if (pos == size)
        {
            curr = head;
            for (int i = 0; i < size - 1; i++)
            {
                curr = curr->getNext();
            }
            newNode->setNext(NULL);
            curr->setNext(newNode);
            curr = curr->getNext();
            tail = curr;
            size++;
        }
        else
        {
            if (pos <= size)
            {
                curr = head;
                for (int i = 0; i < pos - 1; i++)
                {
                    curr = curr->getNext();
                }
                newNode->setNext(curr->getNext());
                curr->setNext(newNode);
                size++;
            }
        }
    }
    else cout << "Error position not correct" << endl ;
}

Node *linkedList::remove(int pos)
{
    if (size != 0 and pos < size)
    {
        if (pos == 0)
        {
            curr = head;
            head = head->getNext();
        }
        else if (pos == size-1)
        {
            curr = head;
            for (int i = 0; i < size - 2; i++)
            {
                curr = curr->getNext();
            }
            curr->setNext(NULL);
        }
        else{
            curr = head;
            for (int i = 0; i < pos-1; i++)
            {
                curr = curr->getNext();
            }
            Node* temp = curr;
            curr = curr->getNext();
            curr = curr->getNext();
            temp->setNext(curr);
        }
    }
    else cout << "Error position not correct" << endl ;
    return head;
}