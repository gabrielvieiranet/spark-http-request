import time

from pyspark.sql import SparkSession
from utils.data_sender import DataSender


class TerminalColors:
    GREEN = '\033[92m'
    RESET = '\033[0m'


def main():
    num_workers = 5
    endpoint = "http://api:5000/"
    retries = 100

    # SparkSession
    spark = SparkSession.builder \
        .appName("Enviar para API") \
        .getOrCreate()

    # Carrega dataset e reparticiona
    df = spark.read.option("header", "true").csv(
        "/opt/bitnami/spark/data/teste.csv")

    df = df.repartition(num_workers)

    # Inicializa DataSender
    data_sender = DataSender(endpoint, retries)

    # Inicia envios HTTP
    start_time = time.time()

    df.foreachPartition(data_sender.send_data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(
        f"Tempo gasto: {TerminalColors.GREEN}"
        f"{elapsed_time:.2f}"
        f"{TerminalColors.RESET} segundos"
    )

    spark.stop()


if __name__ == "__main__":
    main()
