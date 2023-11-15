#include <iostream>
#include <stdexcept>
using namespace std;

// X = 5, Y = 3, Z = 6
// alpha = 6, beta = 7

// recursive
int f67_recursive(int n) {
    if (n >= 0 && n < 42) {
        return n;
    } else if (n >= 42) {
        return f67_recursive(n - 7) + f67_recursive(n - 14) + f67_recursive(n - 21) +\
            f67_recursive(n - 28) + f67_recursive(n - 35) + f67_recursive(n - 42);
    } else {
        throw invalid_argument("n must be non-negative");
    }
}

// tail recursion
int f67_tail_recursion(int n, int a, int b, int c, int d, int e, int f) {
    if (n >= 0 && n < 42) {
        return n;
    } else if (0 <= n - 7 && n - 7 < 42) {
        return a + b + c + d + e + f;
    } else if (n >= 42) {
        return f67_tail_recursion(n - 7, b, c, d, e, f, a + b + c + d + e + f);
    } else {
        throw invalid_argument("n must be non-negative");
    }
}

int f67_tail_recursion_aux(int n) {
    int i = n % 7;
    return f67_tail_recursion(n, i, i + 7, i + 14, i  + 21, i + 28, i + 35);
}

// iterative
int f67_iterative(int n) {
    if (n >= 0 && n < 42) {
        return n;
    }
    int i = n % 7;
    int a = i, b = i + 7, c = i + 14, d = i + 21, e = i + 28, f = i + 35;

    while (n > 42) {
        if (n >= 0 && n < 42) {
            return n;
        }

        int temp = a + b + c + d + e + f;
        a = b;
        b = c;
        c = d;
        d = e;
        e = f;
        f = temp;

        if (n - 7 >= 0 && n - 7 < 42) {
            return temp;
        }

        n -= 7;
    }

    return a + b + c + d + e + f;
}

int main() {
    //int n;
    //cin >> n;
    //cout << f67_recursive(n) << endl;
    //cout << f67_tail_recursion_aux(n) << endl;
    //cout << f67_iterative(n) << endl;

    for (int i = 0; i < 100; i++) {
        //cout << (f67_recursive(i) == f67_tail_recursion_aux(i)) << endl;
        cout << (f67_tail_recursion_aux(i) == f67_iterative(i)) << endl;
    }

    return 0;
}

