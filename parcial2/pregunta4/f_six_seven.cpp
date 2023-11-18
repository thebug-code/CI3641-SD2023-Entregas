#include <iostream>
#include <vector>
#include <stdexcept>
#include <chrono>
#include "matplotlibcpp.h"

using namespace std;
namespace plt = matplotlibcpp;
using namespace std::chrono;

// X = 5, Y = 3, Z = 6
// alpha = 6, beta = 7

/*
 * Fibonacci generalizado recursivo con parametros alpha = 6, beta = 7 
 * @param n: numero a calcular
 * @return: el n-esimo numero de la secuencia
 */
long long int f67_recursive(int n) {
    if (n >= 0 && n < 42) {
        return n;
    } else if (n >= 42) {
        return f67_recursive(n - 7) + f67_recursive(n - 14) + f67_recursive(n - 21) +\
            f67_recursive(n - 28) + f67_recursive(n - 35) + f67_recursive(n - 42);
    } else {
        throw invalid_argument("n must be non-negative");
    }
}


/*
 * Fibonacci generalizado con recursion de cola con parametros alpha = 6, beta = 7
 * @param n: numero a calcular
 * @param a, b, c, d, e, f: valores iniciales de la secuencia
 * @return: el n-esimo numero de la secuencia
 */
long long int f67_tail_recursion(int n, int a, int b, int c, int d, int e, int f) {
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


/*
 * Fibonacci generalizado con recursion de cola con parametros alpha = 6, beta = 7
 * @param n: numero a calcular
 * @return: el n-esimo numero de la secuencia
 */
long long int f67_tail_recursion_aux(int n) {
    int i = n % 7;
    return f67_tail_recursion(n, i, i + 7, i + 14, i  + 21, i + 28, i + 35);
}


/*
 * Fibonacci generalizado iterativo con parametros alpha = 6, beta = 7
 * @param n: numero a calcular
 * @return: el n-esimo numero de la secuencia
 */
long long int f67_iterative(int n) {
    // Casos base
    if (n >= 0 && n < 42) {
        return n;
    }

    // Calculo de los primeros 6 numeros de la secuencia
    int i = n % 7;
    int a = i, b = i + 7, c = i + 14, d = i + 21, e = i + 28, f = i + 35;

    // Calculo del n-esimo numero de la secuencia
    while (n > 42) {
        // Caso base
        if (n >= 0 && n < 42) {
            return n;
        }

        // Calculo de los siguientes 6 numeros de la secuencia
        // y el n-esimo numero de la secuencia
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
    vector<long long int> t1, t2, t3;
    vector<int> ns;

    for (int i = 0; i <= 150; i += 1) {
        // f67_recursive
        auto start = high_resolution_clock::now();
        f67_recursive(i);
        auto stop = high_resolution_clock::now();
        auto d1 = duration_cast<microseconds>(stop - start);
        t1.push_back(d1.count());
        
        // f67_tail_recursion
        start = high_resolution_clock::now();
        f67_tail_recursion_aux(i);
        stop = high_resolution_clock::now();
        auto d2 = duration_cast<microseconds>(stop - start);
        t2.push_back(d2.count());

        // f67_iterative
        start = high_resolution_clock::now();
        f67_iterative(i);
        stop = high_resolution_clock::now();
        auto d3 = duration_cast<microseconds>(stop - start);
        t3.push_back(d3.count());

        // Agrega los tiempos a un vector
        ns.push_back(i);
    }

    // Grafica los tiempos
    plt::figure_size(600, 400);
    plt::named_plot("f67_recursive", ns, t1, "r-");
    plt::named_plot("f67_tail_recursion", ns, t2, "g-");
    plt::named_plot("f67_iterative", ns, t3, "b-");

    plt::title("f67");
    plt::xlabel("n");
    plt::ylabel("t (microseconds)");
    plt::legend();
    plt::save("./f67.png");
    plt::show();

    // Max time
    auto max_time_t1 = *max_element(t1.begin(), t1.end());
    auto max_time_t2 = *max_element(t2.begin(), t2.end());
    auto max_time_t3 = *max_element(t3.begin(), t3.end());

    cout << "max time of f67_recursive: " << max_time_t1 << " microseconds" << endl;
    cout << "max time of f67_tail_recursion: " << max_time_t2 << " microseconds" << endl;
    cout << "max time of f67_iterative: " << max_time_t3 << " microseconds" << endl;

    // Search ns for max time
    int index = distance(t1.begin(), max_element(t1.begin(), t1.end()));
    cout << "ns = " << ns[index] << endl;

    //// tail recursion vs iterative
    t2.clear();
    t3.clear();
    ns.clear();
    for (int i = 2000; i <= 80000; i += 1000) {
        // f67_tail_recursion
        auto start = high_resolution_clock::now();
        f67_tail_recursion_aux(i);
        auto stop = high_resolution_clock::now();
        auto d2 = duration_cast<microseconds>(stop - start);
        t2.push_back(d2.count());

        // f67_iterative
        start = high_resolution_clock::now();
        f67_iterative(i);
        stop = high_resolution_clock::now();
        auto d3 = duration_cast<microseconds>(stop - start);
        t3.push_back(d3.count());

        if (i == 200) {
            cout << f67_iterative(i) << endl;
        }

        // Agrega los tiempos a un vector
        ns.push_back(i);
    }
    
    // Grafica los tiempos
    plt::figure_size(600, 400);
    plt::named_plot("f67_tail_recursion", ns, t2, "g-");
    plt::named_plot("f67_iterative", ns, t3, "b-");

    plt::title("f67");
    plt::xlabel("n");
    plt::ylabel("t (microseconds)");
    plt::legend();
    plt::save("./f67_2.png");
    plt::show();

    // Max time
    max_time_t2 = *max_element(t2.begin(), t2.end());
    max_time_t3 = *max_element(t3.begin(), t3.end());

    cout << endl;
    cout << "max time of f67_tail_recursion: " << max_time_t2 << " microseconds" << endl;
    cout << "max time of f67_iterative: " << max_time_t3 << " microseconds" << endl;

    // Search ns for max time
    index = distance(t2.begin(), max_element(t2.begin(), t2.end()));
    cout << "ns = " << ns[index] << endl;

    return 0;
}
