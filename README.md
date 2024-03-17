# Spark HTTP Request

Este repositório contém um projeto que demonstra como usar o Apache Spark para realizar chamadas HTTP REST distribuídas. Ele inclui um exemplo de código que carrega dados de um arquivo CSV usando o Spark, transforma esses dados e os envia para uma API REST usando a biblioteca requests em Python.

Execute o Docker Compose:

```
docker-compose up --build -d
```

Depois execute o script:

```
./run-job.sh
```

Para entender a diferença, comente a linha abaixo em jobs/main.py:

```
df = df.repartition(5)
```

Note que se não particionamos os dados, eles não podem ser distribuídos entre os workers.