#include <bits/stdc++.h>
#include "Node.h"
#include "LinkedList.h"
using namespace std;

int main(){
    char c;
    linkedList link1;

    Node Node1;
    Node Node2;
    Node Node3;
    Node Node4;
    Node1.setValue(10);
    Node2.setValue(20);
    Node3.setValue(30);
    Node4.setValue(40);
    cout << link1.getSize() << endl;
    link1.insert(&Node1,0);
    link1.insert(&Node2,1);
    link1.insert(&Node3,1);
    link1.insert(&Node4,2);
    cout << link1.gettail();

    // cout << link1.getSize() << endl;
    // link1.curr = link1.head;
    // while (link1.curr != NULL)
    // {
    //     cout << link1.curr->getValue() << endl;
    //     link1.curr = link1.curr->getRight();
    // }

    // // cout << "head : " << link1.head->getValue() << endl;
    // // cout << "tail : " << link1.tail->getValue() << endl;
    // // cout << link1.tail->getLeft()->getValue() << endl;
    // cout << "----------------------" << endl;
    // link1.remove(0);
    // link1.remove(2);

    // cout << link1.getSize() << endl;
    // // cout << link1.head->getValue() << endl;
    // // cout << link1.tail->getValue() << endl;

    // link1.curr = link1.head;
    // while (link1.curr != NULL)
    // {
    //     cout << link1.curr->getValue() << endl;
    //     link1.curr = link1.curr->getRight();
    // }
    return 0;
}