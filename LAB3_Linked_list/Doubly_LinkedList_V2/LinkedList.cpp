#include <bits/stdc++.h>
#include "stack.h"
using namespace std;

linkedList::linkedList()
{
    head = NULL;
    tail = NULL;
    curr = NULL;
    temp = NULL;
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
            curr = curr->getRight();
        }
        temp = curr->getRight();
        curr->setRight(newNode);
        temp->setLeft(newNode);
        newNode->setLeft(curr);
        newNode->setRight(temp);
        size+=1;
    }
}

Node *linkedList::remove(int pos)
{
    if(pos > (size+1) or pos <= 0){cout << "Error : can't remove this position" << endl;}
    else{
        curr = head;
        for (int i = 0; i < pos-1; i++){
            curr = curr->getRight();
        }
        temp = curr->getRight();
        curr->setRight(temp->getRight());
        curr = curr->getRight();
        curr->setLeft(temp->getLeft());
        temp->setRight(NULL);
        temp->setLeft(NULL);
        size-=1;
    }
    
    return head;
}