# Análisis del rendimiento de docker aplicado a Data Science

1. Se realiza el clone al repositorio de github https://github.com/djulcac/uni-seminario-1-docker

        $ git clone https://github.com/djulcac/uni-seminario-1-docker.git
2. Creación de la imagen docker de nombre seminario1

        $ docker build --tag=seminario1 .
3. Correr el programa

        $ docker run seminario1
4. Para acceder al bash de la imagen

        $ docker run -it seminario1 /bash/bin
5. Para pasar una carpeta del host y correr el programa

        $ docker run -v \$PWD:/opt seminario1 /bin/bash -c "python /opt/app.py"