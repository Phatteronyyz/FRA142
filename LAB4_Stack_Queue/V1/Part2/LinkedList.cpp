#include <bits/stdc++.h>
#include "LinkedList.h"
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
    if(pos > (size+1) or pos <= 0){cout << "Error : can't insert to this position" << endl;}
    else{
        curr = head;
        for (int i = 0; i < pos-1; i++){
            curr = curr->getNext();
        }
        newNode->setNext(curr->getNext());
        curr->setNext(newNode);
        size+=1;
    }
}

Node *linkedList::remove(int pos)
{
    if(pos > size or pos <= 0){cout << "Error : can't remove this position" << endl;}
    else{
        curr = head;
        Node *temp;
        for (int i = 0; i < pos-1; i++){
            curr = curr->getNext();
        }
        temp = curr->getNext();
        curr->setNext(temp->getNext());
        temp->setNext(NULL);
        size -= 1;
    }
    return curr;
}