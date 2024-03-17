import requests


class DataSender:
    def __init__(self, endpoint, retries):
        self.endpoint = endpoint
        self.retries = retries

    def send_data(self, rows):
        for row in rows:
            data = {
                "id": row.id,
                "produto": row.produto,
                "ativo": row.ativo
            }
            attempts = 0
            while attempts <= self.retries:
                response = requests.post(self.endpoint, json=data)
                if response.status_code != 200:
                    attempts += 1
                else:
                    break
            if attempts > self.retries:
                print(f"Falha após {self.retries + 1} tentativas. Desistindo.")
