# Spark HTTP Request

![Apache Spark](/img/spark.png)

Este repositório contém um projeto que demonstra como usar o Apache Spark para realizar chamadas HTTP REST distribuídas. Ele inclui um exemplo de código que carrega dados de um arquivo CSV, transforma esses dados e os envia para uma API REST usando a biblioteca requests em Python.

Execute o Docker Compose:

```
docker-compose up --build -d
```

Depois execute o script:

```
./run-job.sh
```

Para entender a diferença, comente a linha abaixo em jobs/main.py e rode o script novamente:

```
df = df.repartition(num_workers)
```

Você vai ver que agora ficou mais lento porque não particionamos os dados e eles não foram distribuídos entre os workers.