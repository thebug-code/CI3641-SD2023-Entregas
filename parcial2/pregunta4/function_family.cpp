#include <iostream>
#include <stdexcept>
using namespace std;

// X = 5, Y = 3, Z = 6
// alpha = 6, beta = 7

int f_six_seven_recursion(int n) {
    if (n >= 0 && n < 42) {
        return n;
    } else if (n >= 42) {
        return f_six_seven_recursion(n - 7) + f_six_seven_recursion(n - 14) \
            + f_six_seven_recursion(n - 21) + f_six_seven_recursion(n - 28) \
            + f_six_seven_recursion(n - 35) + f_six_seven_recursion(n - 42);
    } else {
        throw invalid_argument("n must be non-negative");
    }
}

int main() {
    int n;
    cin >> n;
    cout << f_six_seven_recursion(n) << endl;
    return 0;
}

