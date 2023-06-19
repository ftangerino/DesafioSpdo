from pymongo import MongoClient
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

#Realizando a conexão com o mongo
connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
db_connection = client["Estabelecimentos"]

## Verifica a conexão
print(db_connection)

## Verifica a coleção
collection = db_connection.get_collection("Estabelecimentos0")
print(collection)


#Código para fazer a correlação dos documentos CNAE PRINCIAPL E SECUNDARIO

chunk_size = 10000
limit_documents = 1000


pipeline = [
    {'$limit': limit_documents},
    {
        '$group': {
            '_id': {
                'CNAE_PRINCIPAL': '$CNAE FISCAL PRINCIPAL',
                'CNAE_SECUNDARIA': '$CNAE FISCAL SECUNDARIA'
            },
            'count': {'$sum': 1}
        }
    },
    {
        '$group': {
            '_id': '$_id.CNAE_PRINCIPAL',
            'correlation': {
                '$push': {
                    'CNAE_PRINCIPAL': '$_id.CNAE_PRINCIPAL',
                    'CNAE_SECUNDARIA': '$_id.CNAE_SECUNDARIA',
                    'count': '$count'
                }
            }
        }
    }
]

# Lista para armazenar os chunks processados
chunks = []

# Iterar sobre os documentos em chunks
for chunk in collection.aggregate(pipeline, allowDiskUse=True, batchSize=chunk_size):
    chunks.append(pd.DataFrame(chunk))

# Concatenar os DataFrames dos chunks em um DataFrame final
df_final = pd.concat(chunks, ignore_index=True)

# Exportar DataFrame final para arquivo CSV
df_final.to_csv('tabela_correlacao.csv', index=False)


# Ler o arquivo CSV
df = pd.read_csv('tabela_correlacao.csv')

# Criar um novo arquivo Excel
wb = Workbook()
ws = wb.active

# Escrever os dados no arquivo Excel com formatação
for r in dataframe_to_rows(df, index=False, header=True):
    ws.append(r)
# Salvar o arquivo Excel
wb.save('tabela_correlacao.xlsx')