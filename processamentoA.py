from pymongo import MongoClient

#Realizando a conexão com o mongo
connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
db_connection = client["Estabelecimentos"]

## Verifica a conexão
print(db_connection)

## Verifica a coleção
collection = db_connection.get_collection("Estabelecimentos0")
print(collection)


##Calculo Porcentagem empresas ativas
total_empresas = collection.count_documents({}, limit=5000)
print(total_empresas)
print()

total_empresas_ativas = collection.count_documents({'SITUACAO CADASTRAL': 2}, limit=5000)
print(total_empresas_ativas)

porcentagem_empresas_ativas = (total_empresas_ativas / total_empresas) * 100

print(f"Porcentagem de empresas ativas: {porcentagem_empresas_ativas}%")

