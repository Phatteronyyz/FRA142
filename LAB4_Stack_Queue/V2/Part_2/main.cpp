#include <bits/stdc++.h>
#include "Stack.h"
#include "Queue.h"
using namespace std;

int main(){
    Stack st;
    Queue q;

    cout << "-------Stack-------" << endl;
    st.push(10);
    st.push(12);
    st.push(20);
    st.pop();
    st.push(30);
    st.pop();
    st.push(99);
    st.pop();
    cout << st.getSize() << endl;
    cout << "Top : " << st.peek() << endl;

    cout << "-------Queue-------" << endl;
    q.enqueue(10);
    q.enqueue(30);
    q.dequeue();
    q.dequeue();
    q.enqueue(55);
    cout << "Top : " << q.peek() << endl;



    return 0;
}