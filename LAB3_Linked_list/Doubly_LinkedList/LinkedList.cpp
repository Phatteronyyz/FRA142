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
        if (pos == 0 and size == 0)
        {
            curr = newNode;
            newNode->setRight(NULL);
            newNode->setLeft(NULL);
            head = curr;
            tail = curr;
            size+=1;
            cout << "add " << newNode->getValue() << " at first element" << endl;
        }
        else if (pos == 0)
        {
            curr = newNode;
            newNode->setRight(head);
            newNode->setLeft(NULL);
            curr->getRight()->setLeft(curr);
            head = curr;
            size+=1;
            cout << "add "<< newNode->getValue() <<" to first position" << endl;
        }
        else if (pos == size)
        {
            curr = head;
            for (int i = 0; i < size - 1; i++)
            {
                curr = curr->getRight();
            }
            newNode->setRight(NULL);
            curr->setRight(newNode);
            newNode->setLeft(curr);
            curr = curr->getRight();
            tail = curr;
            size+=1;
            cout << "add " << newNode->getValue() << " to last position" << endl;
        }
        else
        {
            if (pos <= size)
            {
                curr = head;
                for (int i = 0; i < pos - 1; i++)
                {
                    curr = curr->getRight();
                }
                newNode->setRight(curr->getRight());
                newNode->setLeft(curr);
                curr->getRight()->setLeft(newNode);
                curr->setRight(newNode);
                size+=1;
                cout << "add " << newNode->getValue() << " to position " << pos << endl;
            } 
            else cout << "Error, position not correct can't insert to this position" << endl ;
        }
}

Node *linkedList::remove(int pos)
{
    if (size != 0 and pos < size)
    {
        if (pos == 0)
        {
            Node *temp;
            temp = head;
            curr = head;
            head = head->getRight();
            size -= 1;
            cout << "remove " << temp->getValue() << " from first position" << endl;
        }
        else if (pos == size-1)
        {
            Node *temp;
            temp = tail;
            curr = tail->getLeft();
            tail->setLeft(NULL);
            tail = curr;
            curr->setRight(NULL);
            size -= 1;
            cout << "remove " << temp->getValue() << " from last position" << endl;
        }
        else{
            curr = head;
            Node *tempp;
            for (int i = 0; i < pos-1; i++)
            {
                curr = curr->getRight();
            }
            Node *temp;
            tempp = curr->getRight();
            temp = curr->getRight();
            curr->setRight(temp->getRight());
            curr = curr->getRight();
            curr->setLeft(temp->getLeft());
            temp->setRight(NULL);
            temp->setLeft(NULL);
            size -= 1;
            cout << "remove " << tempp->getValue() << " from position " << pos << endl;
        }
    }
    else cout << "Error, position not correct can't remove this position" << endl ;
    return head;
}

Node* linkedList::gettail(){
    return tail;
}