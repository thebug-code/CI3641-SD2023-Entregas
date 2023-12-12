/*
 * Dado dos arreglos de enteros de igual tamaño, calcular el producto punto
 * usando de forma concurrente
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>
#include <math.h>

/* Estructura para pasar los argumentos a los hilos */
typedef struct {
    int *v1;
    int *v2;
    int start;
    int num_computations;
    int result;
} dot_product_args;

void *computeDotProduct(void *arg);

int main(int argc, char *argv[]) {
    int N;                   /* Tamaño de los arreglos */
    int num_threads;         /* Número de hilos */
    int remainder;           /* Residuo */
    int chunk;               /* Cantidad de productos punto por hilo */
    int *v1;                 /* Arreglo de enteros */
    int *v2;                 /* Arreglo de enteros */
    int i;                   /* Iterador */
    int seq_dot_product;     /* Producto punto secuencial */
    int array_index;         /* Índice para el arreglo */
    int dot_product;         /* Producto punto */
    pthread_t *threads       /* Arreglo de hilos */;
    dot_product_args **args; /* Arreglo de argumentos para los hilos */
    
    if (argc != 3) {
        printf("Uso: %s <tamaño del arreglo> <número de hilos>\n", argv[0]);
        exit(-1);
    }

    /* Valores iniciales */
    N = atoi(argv[1]);
    num_threads = atoi(argv[2]);

    /* Calcula cuantos productos punto se deben calcular por hilo */
    remainder = N % num_threads;
    chunk = (N - remainder) / num_threads;

    /* Crea los arreglos */
    v1 = (int *) malloc(N * sizeof(int));
    v2 = (int *) malloc(N * sizeof(int));


    /* Inicializa los arreglos */
    seq_dot_product = 0;
    for (i = 0; i < N; i++) {
        v1[i] = rand() % 100;
        v2[i] = rand() % 100;
        seq_dot_product += v1[i] * v2[i];
    }

    printf("El producto punto secuencial es %d\n", seq_dot_product);

    /* Crea el arreglo de punteros a hilos */
    threads = (pthread_t *) malloc(num_threads * sizeof(pthread_t));

    /* Crea el arreglo de argumentos para los hilos */
    args = (dot_product_args **) malloc(num_threads * sizeof(args));

    array_index = 0;
    /* Crea los hilos */
    for (i = 0; i < num_threads; i++) {
        dot_product_args *arg = (dot_product_args *) malloc(sizeof(dot_product_args));
        arg->v1 = v1;
        arg->v2 = v2;
        arg->start = array_index;
        arg->num_computations = chunk;
        arg->result = 0;

        /* Si hay un residuo, se le asigna un producto punto al hilo */
        if (remainder > 0) {
            arg->num_computations++;
            remainder--;
        }

        /* Actualiza el índice para el siguiente hilo */
        array_index += arg->num_computations;

        args[i] = arg;

        /* Crea el hilo */
        if (pthread_create(&threads[i], NULL, computeDotProduct, (void *) args[i])) {
            printf("Error al crear el hilo %d\n", i);
            exit(-1);
        }
    }

    /* Espera a que los hilos terminen */
    for (i = 0; i < num_threads; i++) {
        void *status;
        if (pthread_join(threads[i], &status)) {
            printf("Error al esperar por el hilo %d\n", i);
            exit(-1);
        }
    }

    /* Calcula el producto punto */
    dot_product = 0;
    for (i = 0; i < num_threads; i++) {
        dot_product += args[i]->result;
    }
    printf("El producto punto es %d\n", dot_product);

    /* Libera la memoria */
    free(v1);
    free(v2);

    for (i = 0; i < num_threads; i++) {
        free(args[i]);
    }

    free(args);
    free(threads);

    return 0;
}

/* Función que calcula el producto punto */
void *computeDotProduct(void *this_arg) {
    int i;
    dot_product_args *arg = (dot_product_args *) this_arg;
    for (i = 0; i < arg->num_computations; i++) {
        arg->result += arg->v1[i + arg->start] * arg->v2[i + arg->start];
    }
    return NULL;
}
