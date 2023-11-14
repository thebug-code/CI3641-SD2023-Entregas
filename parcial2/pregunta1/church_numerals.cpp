// Church numerals

#include <iostream>
using namespace std;

// Constructor para representar el cero
auto Cero = [](auto) {
    return [](auto x) {
        return x;
    };
};

// Constructor para representar el sucesor
auto Suc(auto a) {
    return [=](auto f) {
        return [=](auto x) {
            return f(a(f)(x));
        };
    };
};

// Constructor para representar la suma
auto Sum(auto a, auto b) {
    return [=](auto f) {
        return [=](auto x) {
            return a(f)(b(f)(x));
        };
    };
};

// Constructor para representar la multiplicación
auto Mul(auto a, auto b) {
    return [=](auto f) {
        return a(b(f));
    };
};

int main() {
    // Representación del número 3
    auto tres = Suc(Suc(Suc(Cero)));

    // Representación del número 4
    auto cuatro = Suc(tres);

    cout << "3 + 4 = " << Sum(tres, cuatro)([](auto x) { return x + 1; })(0) << endl;
    cout << "3 * 4 = " << Mul(tres, cuatro)([](auto x) { return x + 1; })(0) << endl;
}
