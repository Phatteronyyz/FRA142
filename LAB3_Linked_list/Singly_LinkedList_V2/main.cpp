#include <bits/stdc++.h>
#include "Node.h"
#include "LinkedList.h"
using namespace std;

void print(linkedList ll){
    ll.curr = ll.head->getNext();
    while (ll.curr != ll.tail)
    {
        cout << ll.curr->getValue() << " ";
        ll.curr = ll.curr->getNext();
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
    ll.head->setNext(&tailNode);
    tailNode.setNext(NULL);

    //main
    Node node1;
    Node node2;
    Node node3;
    Node node4;
    node1.setValue(10);
    node2.setValue(20);
    node3.setValue(30);
    node4.setValue(40);
    ll.insert(&node1,1);
    ll.insert(&node2,1);
    ll.insert(&node3,2);
    ll.insert(&node4,3);
    ll.remove(1);
    ll.remove(2);
    ll.remove(2);

    print(ll);
    
    return 0;
}