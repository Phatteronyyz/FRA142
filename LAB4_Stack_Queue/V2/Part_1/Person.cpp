#include "Person.h"
#include <iostream>
using namespace std;

// ***************************-Person-***************************
Person::Person(){
    name = "";
    height = 0;
    age = 0;
}
Person::Person(string n, int h, int a){
    name = n;
    height = h;
    age = a;
}
Person::~Person(){

}
void Person::showPersonInfo(){
    cout<<"Person name:"<<name<<endl;
    cout<<"height:"<<height<<endl;
    cout<<"age:"<<age<<endl;
}

// ***************************-Student-***************************

Student::Student():Person(){
    id = 0;
    grade = 0;
}

Student::Student(string name, int height, int age, int i,int g):Person(name, height, age){
    id = i;
    grade = g;
}

Student::~Student(){

}
void Student::showStudenInfo(){
    showPersonInfo();
    cout<<"id:"<<id<<endl;
    cout<<"grade:"<<grade<<endl;
}

// ***************************-Teacher-***************************

Teacher::Teacher():Person(){
    subject = "";
}

Teacher::Teacher(string n, int h, int a, string s):Person(n, h, a){
    subject = s;
}

Teacher::~Teacher(){

}

void Teacher::setSubject(string newSubject){
    subject = newSubject;
}

string Teacher::getSubject(){
    return subject;
}

void Teacher::showTeacherInfo(){
    showPersonInfo();
    cout << "subject:" << subject << endl;
}


