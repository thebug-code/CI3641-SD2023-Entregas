# Algoritmo de fibonacci generalizado
Este proyecto implementa el algoritmo de Fibonacci generalizado (de cola, recursivo e iterativo) con parámetros `alpha=6` y `beta=7` y proporciona una visualización de los tiempos de ejecución utilizando Matplotlib para C++.

## Requisitos previos
Para ejecutar el programa y visualizar los tiempos, se requiere una versión específica de Python. A continuación, se detallan los pasos para configurar el entorno.

1. Configuración de pyenv y pyenv-virtualenv

    Clone pyenv:
    
    ```
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    ```
    
    Agregue la configuración a ~/.zshrc (o ~/.bashrc si estás utilizando Bash):
    
    ```
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/repo/prj
    if command -v pyenv 1>/dev/null 2>&1; then
      eval "$(pyenv init --path)"
    fi
    ```
    
    Reinicie la terminal y clone pyenv-virtualenv:
    ```
    git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
    ```
    
    Agregue la configuración de pyenv-virtualenv a ~/.zshrc:
    ```
    eval "$(pyenv virtualenv-init -)"
    ```

2. Instalación de Python 3.6.0 y configuración de entorno virtual

    Instale Python 3.6.0:
    ```
    pyenv install --patch 3.6.0 < alignment.patch
    ```
    
    Cree un entorno virtual:
    ```
    pyenv virtualenv 3.6.0 <env-name>
    ```
    
    Active el entorno virtual:
    ```
    pyenv activate <env-name>
    ```

3. Configuración del proyecto

    Clone el repositorio:
    ```
    git clone git@github.com:thebug-code/CI3641-SD2023-Entregas.git
    ```
    
    Navegue al directorio del proyecto:
    ```
    cd CI3641-SD2023-Entregas/parcial2/pregunta4
    ```
    
    Instale las dependencias:
    ```
    pip install -r requirements.txt
    ```

4. Configuración de la variable PYTHONPATH
    Configure la variable PYTHONPATH como se muestra a continuación, reemplazando {USER} con el nombre de usuario de su máquina:
    
    ```
    export PYTHONPATH="/home/{user}/.pyenv/versions/3.6.0/envs/py2/lib/python3.6/site-packages"
    ```

5. Compilación y Ejecución del Programa C++

    Compile el programa:
    
    ```
    g++ function_family.cpp -std=c++11 -I/home/{user}/.pyenv/versions/3.6.0/include/python3.6m -I/home/{user}/.pyenv/versions/py2/lib/python3.6/site-packages/numpy/core/include -L/home/{user}/.pyenv/versions/3.6.0/lib -lpython3.6m
    ```

    Ejecute el programa:
    
    ```
    ./a.out
    ```

¡Listo! Ahora deberías poder ejecutar y visualizar los tiempos de ejecución del algoritmo de Fibonacci generalizado en sus distintas versiones. Si encuentras algún problema, asegúrate de seguir los pasos detallados y verifica la configuración de tu entorno. ¡Buena suerte! 🙂
