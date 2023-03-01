#include <bits/stdc++.h>
#include "Queue.h"
using namespace std;

Queue :: Queue():linkedList(){

}

Queue :: ~Queue(){

}

void Queue :: enqueue(Node *newNode){
    insert(newNode,0);
}

Node *Queue :: dequeue(){
    remove((getSize()-1));
}

int Queue :: peek(){
    return tail->getValue();
}