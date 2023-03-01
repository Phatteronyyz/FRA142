#include "Person.h"
#include<iostream>
using namespace std;

int main(){

    // add code here
    Person *me = new Person("Tengnueng", 18, 170);
    me->showPersonInfo();

    Student *teng2 = new Student("Tengsong", 19 ,168, 74 ,10);
    teng2->showStudenInfo();

    Teacher *khunkru = new Teacher("Bink", 30, 175, "Programming");
    khunkru->showTeacherInfo();
    khunkru->setSubject("Math");
    cout << khunkru->getSubject();

    return 0;
}
