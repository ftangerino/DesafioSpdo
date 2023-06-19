from pymongo import MongoClient
import pandas as pd
import csv

#Realizando a conexão com o mongo
connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
db_connection = client["Estabelecimentos"]

## Verifica a conexão
print(db_connection)

## Verifica a coleção
collection = db_connection.get_collection("Estabelecimentos0")
print(collection)


##Lista

limit_documents = 100000

# Definir o nome do arquivo CSV de saída
output_file = 'resultado.csv'


estagios = [
    {'$limit': limit_documents},
    {"$match": {
        "$expr": {
            "$regexMatch": {
                "input": {"$toString": "$CNAE FISCAL PRINCIPAL"},
                "regex": "^561"  # Prefixo do CNAE PRINCIPAL para restaurantes
            }
        }
    }},
    {"$group": {
        "_id": {"$substr": [{"$toString": "$DATA DE INICIO ATIVIDADE"}, 0, 4]},  # Extrair os primeiros 4 caracteres como ano
        "count": {"$sum": 1}  # Contar a quantidade de documentos em cada grupo
    }},
    {"$sort": {"_id": 1}}  # Ordenar os resultados por ano
]

# Executar a agregação no banco de dados
result = list(collection.aggregate(estagios))
df = pd.DataFrame(result)
df = df.rename(columns={"_id": "ano", "count": "quantidade"})

# Escrever os resultados em um arquivo CSV
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Ano', 'Quantidade'])
    for doc in result:
        writer.writerow([doc['_id'], doc['count']])

print(f"Arquivo CSV gerado com sucesso: {output_file}")


output_file = 'resultado.xlsx'

# Salvar DataFrame em um arquivo Excel
df.to_excel(output_file, index=False)

print(f"Arquivo Excel gerado com sucesso: {output_file}")