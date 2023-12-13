#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <pthread.h>
#include <unistd.h> 

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
int file_count = 0;

void *count_files(void *arg) {
    DIR *dir;             /* Puntero al directorio */
    struct dirent *entry; /* Puntero a la entrada */
    char *path;           /* Path del directorio */
    char *subpath;        /* Path del subdirectorio */
    pthread_t thread;     /* Identificador del hilo */
    void *status;         /* Estado devuelto por el hilo */

    path = (char *) arg;
    
    /* Abre el directorio actual */
    if (!(dir = opendir(path))) {
        perror("opendir");
        pthread_exit(NULL);
    }

    /* Cuenta el número de archivos en el directorio */
    if (access(path, F_OK) != -1 ){
        while ((entry = readdir(dir))) {
            if (entry->d_type == DT_REG) {
                printf("%d) - %s\n", file_count + 1, entry->d_name);
                pthread_mutex_lock(&mutex);
                file_count++;
                pthread_mutex_unlock(&mutex);
            } else if (entry->d_type == DT_DIR && strcmp(entry->d_name, ".") && strcmp(entry->d_name, "..")) {
                subpath = malloc(strlen(path) + strlen(entry->d_name) + 2);

                /* Construye el path del subdirectorio */
                sprintf(subpath, "%s/%s", path, entry->d_name);

                /* Crea un hilo para contar los archivos del subdirectorio */
                pthread_create(&thread, NULL, count_files, (void *) subpath); 

                /* Espera a que el hilo termine */
                if (pthread_join(thread, &status)) {
                    perror("pthread_join");
                    pthread_exit(NULL);
                }

                free(subpath);
            }
        }
        closedir(dir);
    } else {
        perror("access");
        pthread_exit(NULL);
    }
    
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t tid;
    void *status;

    if (argc != 2) {
        fprintf(stderr, "Uso: %s <path>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    

    pthread_create(&tid, NULL, count_files, (void *) argv[1]);
    pthread_join(tid, &status);
    printf("Numero total de archivos %d\n", file_count);

    return 0;
}
