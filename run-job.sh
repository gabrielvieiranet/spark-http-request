#!/bin/bash

# Nome do container do Spark
SPARK_CONTAINER_NAME="spark-http-spark-master-1"

# Caminho do script Python no container
PYTHON_SCRIPT_PATH="/opt/bitnami/spark/scripts/main.py"

# Executando o script Python no container Spark
docker exec -it $SPARK_CONTAINER_NAME /opt/bitnami/spark/bin/spark-submit $PYTHON_SCRIPT_PATH