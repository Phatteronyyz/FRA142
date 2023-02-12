#ifndef NODE_H
#define NODE_H
class Node{
    private:
        int value;
        Node *right;
        Node *left;
        
    public:
        Node();
        Node(int newValue, Node *newRight, Node *newLeft);
        void print();
        int getValue();
        void setValue(int newValue);
        void setRight(Node *newRight);
        Node *getRight();
        void setLeft(Node *newLeft);
        Node *getLeft();
        
};
#endif