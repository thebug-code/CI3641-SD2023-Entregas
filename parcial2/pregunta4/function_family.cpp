#include <iostream>
#include <stdexcept>
using namespace std;

// X = 5, Y = 3, Z = 6
// alpha = 6, beta = 7

// recursive
int f_six_seven_recursive(int n) {
    if (n >= 0 && n < 42) {
        return n;
    } else if (n >= 42) {
        return f_six_seven_recursive(n - 7) + f_six_seven_recursive(n - 14) \
            + f_six_seven_recursive(n - 21) + f_six_seven_recursive(n - 28) \
            + f_six_seven_recursive(n - 35) + f_six_seven_recursive(n - 42);
    } else {
        throw invalid_argument("n must be non-negative");
    }
}

// tail recursion
int f_six_seven_tail_recursion(int n, int a, int b, int c, int d, int e, int f) {
    if (n >= 0 && n < 42) {
        return n;
    } else if (0 <= n - 7 && n - 7 < 42) {
        return a + b + c + d + e + f;
    } else if (n >= 42) {
        return f_six_seven_tail_recursion(n - 7, b, c, d, e, f, a + b + c + d + e + f);
    } else {
        throw invalid_argument("n must be non-negative");
    }
}

int f_six_seven_tail_recursion_aux(int n) {
    int i = n % 7;
    return f_six_seven_tail_recursion(n, i, i + 7, i + 14, i  + 21, i + 28, i + 35);
}


int main() {
    int n;
    cin >> n;
    cout << f_six_seven_recursive(n) << endl;
    cout << f_six_seven_tail_recursion_aux(n) << endl;
    return 0;
}

