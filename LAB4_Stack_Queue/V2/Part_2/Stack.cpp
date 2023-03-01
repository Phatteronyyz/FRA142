#include <bits.stdc++.h>
#include "Stack.h"
using namespace std;

Stack :: Stack(){

}

Stack :: ~Stack(){

}

void Stack :: push(Node *newNode){
    insert(*newNode,0);
}

Node Stack :: pop(){
    remove(0);
    return 
}

Node Stack :: peek(){
    return head->getValue();
}