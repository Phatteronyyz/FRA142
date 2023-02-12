#include <bits/stdc++.h>
#include "Node.h"
#include "LinkedList.h"
using namespace std;

int main(){
    Node Node1;
    Node Node2;
    Node Node3;
    Node Node4;
    linkedList link1;
    Node1.setValue(10);
    Node2.setValue(20);
    Node3.setValue(30);
    Node4.setValue(40);
    link1.insert(&Node1, 0);
    link1.insert(&Node2, 0);
    link1.insert(&Node3, 2);
    link1.insert(&Node4, 1);

    link1.curr = link1.head;
    while (link1.curr != NULL)
    {
        cout << link1.curr->getValue() << endl;
        link1.curr = link1.curr->getNext();
    }

    link1.remove(3);

    cout << "----------------------" << endl;

    link1.curr = link1.head;
    while (link1.curr != NULL)
    {
        cout << link1.curr->getValue() << endl;
        link1.curr = link1.curr->getNext();
    }
    return 0;
}