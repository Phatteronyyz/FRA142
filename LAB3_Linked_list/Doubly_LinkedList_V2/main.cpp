#include <bits/stdc++.h>
#include "Node.h"
#include "LinkedList.h"
using namespace std;

void print(linkedList ll){
    ll.curr = ll.head->getRight();
    while (ll.curr != ll.tail)
    {
        cout << ll.curr->getValue() << " ";
        ll.curr = ll.curr->getRight();
    }
    cout << "\n" << "size : " << ll.getSize() << endl;
}

int main(){

    linkedList ll;

    //setup
    Node headNode;
    Node tailNode;
    ll.head = &headNode;
    ll.tail = &tailNode;
    ll.head->setRight(&tailNode);
    ll.head->setLeft(NULL);
    ll.tail->setRight(NULL);
    ll.tail->setLeft(&headNode);

    //main
    Node node1;
    Node node2;
    Node node3;
    node1.setValue(10);
    node2.setValue(20);
    node3.setValue(30);
    ll.insert(&node1,1);
    ll.insert(&node2,1);
    ll.insert(&node3,3);

    ll.remove(3);

    print(ll);

    return 0;
}