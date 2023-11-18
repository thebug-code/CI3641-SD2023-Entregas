#include <iostream>
using namespace std;

// Structura que representa un numero de Church
struct ChurchNumeral {
    virtual int value() const = 0;
    virtual ChurchNumeral* clone() const = 0;

    // Operaciones
    virtual ChurchNumeral* add(const ChurchNumeral& other) const = 0;
    virtual ChurchNumeral* multiply(const ChurchNumeral& other) const = 0;
};


// Estructura que representa el numero 0
struct Zero : public ChurchNumeral {
    int value() const override { return 0; }
    ChurchNumeral* clone() const override { return new Zero(); }
    ChurchNumeral* add(const ChurchNumeral& other) const override { return other.clone(); }
    ChurchNumeral* multiply(const ChurchNumeral& other) const override { return new Zero(); }
};

// Estructura que representa el numero n + 1
struct Succ : public ChurchNumeral {
    const ChurchNumeral* predecessor;

    Succ(const ChurchNumeral* predecessor) : predecessor(predecessor) {}

    int value() const override { return predecessor->value() + 1; }
    ChurchNumeral* clone() const override { return new Succ(predecessor->clone()); }
    ChurchNumeral* add(const ChurchNumeral& other) const override { return new Succ(predecessor->add(other)); }
    ChurchNumeral* multiply(const ChurchNumeral& other) const override { return predecessor->multiply(other)->add(other); }
};


// Main
int main() {
    ChurchNumeral* zero = new Zero();
    ChurchNumeral* one = new Succ(zero);
    ChurchNumeral* two = new Succ(one);
    ChurchNumeral* three = new Succ(two);

    cout << three->value() << endl;
    cout << one->value() << endl;
    cout << two->value() << endl;
    cout << three->value() << endl;
    
    cout << three->add(*zero)->value() << endl; // Output: 3
    cout << three->add(*two)->value() << endl; // Output: 5
    cout << three->multiply(*two)->value() << endl; // Output: 6
    
    delete zero;
    delete one;
    delete two;
    delete three;
}
