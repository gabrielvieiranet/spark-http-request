import requests
from pyspark.sql import SparkSession


def send_to_api(rows):
    api_endpoint = "http://api:5000/"
    for row in rows:

        data = {
            "id": row.id,
            "produto": row.produto,
            "ativo": row.ativo
        }
        response = requests.post(api_endpoint, json=data)
        if response.status_code != 200:
            print(
                f"Erro. Status: {response.status_code}")
        else:
            print(response.content)


def main():

    # SparkSession
    spark = SparkSession.builder \
        .appName("Enviar para API") \
        .getOrCreate()

    df = spark.read.option("header", "true").csv(
        "/opt/bitnami/spark/data/teste.csv")

    # particionando os dados para distribuir entre os workers
    df = df.repartition(5)

    df.foreachPartition(send_to_api)

    spark.stop()


if __name__ == "__main__":
    main()
