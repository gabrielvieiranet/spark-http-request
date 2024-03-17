#!/bin/bash

# Nome do container do Spark
SPARK_CONTAINER_NAME="spark-http-spark-master-1"

# Caminho base
BASE_PATH="/opt/bitnami/spark/scripts"

cd jobs || exit

# Zipa o diretório de utilitários
zip -r "utils.zip" "utils"

# Executando o script Python no container Spark
docker exec -it $SPARK_CONTAINER_NAME /opt/bitnami/spark/bin/spark-submit --py-files "$BASE_PATH/utils.zip" "$BASE_PATH/main.py"