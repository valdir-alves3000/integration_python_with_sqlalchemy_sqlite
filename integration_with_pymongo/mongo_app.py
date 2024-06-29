import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongo_uri)
db = client['bank']
collection = db['clients']


cliente_document = {
    "nome": "João Silva",
    "cpf": "123456789",
    "endereco": "Rua A",
    "contas": [
        {"tipo": "Corrente", "agencia": "0001", "num": 12345, "saldo": 1000.0}
    ]
}

collection.insert_one(cliente_document)


def get_all_clients():
    return list(collection.find())

def get_client_by_cpf(cpf):
    return collection.find_one({"cpf": cpf})


clients = get_all_clients()
for client in clients:
    print(client['nome'], client['cpf'], client['endereco'])
    for conta in client['contas']:
        print(f"Conta {conta['tipo']} com saldo de {conta['saldo']}")

client = get_client_by_cpf("123456789")
if client:
    print(client['nome'], client['cpf'], client['endereco'])
    for conta in client['contas']:
        print(f"Conta {conta['tipo']} com saldo de {conta['saldo']}")
