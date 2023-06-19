import pandas as pd


# Nome das colunas do arquivo empresas.csv
empresColunas = [
    'CNPJ BASICO', 'RAZAO SOCIAL/NOME EMPRESARIAL', 'NATUREZA JURIDICA',
    'QUALIFICACAO DO RESPONSAVEL', 'CAPITAL SOCIAL DA EMPRESA',
    'PORTE DA EMPRESA', 'ENTE FEDERATIVO RESPONSAVEL'
]

# Nome das colunas do arquivo estabelecimento.csv
estabelColunas = [
     'CNPJ BASICO', 'CNPJ ORDEM', 'CNPJ DV', 'IDENTIFICADOR MATRIZ/FILIAL',
     'NOME FANTASIA', 'SITUACAO CADASTRAL', 'DATA SITUACAO CADASTRAL',
     'MOTIVO SITUACAO CADASTRAL', 'NOME DA CIDADE NO EXTERIOR', 'PAIS',
     'DATA DE INICIO ATIVIDADE', 'CNAE FISCAL PRINCIPAL',
     'CNAE FISCAL SECUNDARIA', 'TIPO DE LOGRADOURO', 'LOGRADOURO', 'NUMERO',
     'COMPLEMENTO', 'BAIRRO', 'CEP', 'UF', 'MUNICIPIO', 'DDD 1', 'TELEFONE 1',
     'DDD 2', 'TELEFONE 2', 'DDD DO FAX', 'FAX', 'CORREIO ELETRONICO',
     'SITUACAO ESPECIAL', 'DATA DA SITUACAO ESPECIAL'
]

socioColunas = [
    'CNPJ BASICO', 'IDENTIFICADOR DE SOCIO',
    'NOME DO SOCIO (NO CASO PF) OU RAZAO SOCIAL (NO CASO PJ)',
    'CNPJ/CPF DO SOCIO', 'QUALIFICACAO DO SOCIO', 'DATA DE ENTRADA SOCIEDADE',
    'PAIS', 'REPRESENTANTE LEGAL', 'NOME DO REPRESENTANTE',
    'QUALIFICACAO DO REPRESENTANTE LEGAL', 'FAIXA ETARIA'
]

estabelCSV = [ 'Estabelecimentos0.csv', 'Estabelecimentos1.csv', 'Estabelecimentos2.csv',
            'Estabelecimentos3.csv', 'Estabelecimentos4.csv' , 'Estabelecimentos5.csv',
            'Estabelecimentos6.csv', 'Estabelecimentos7.csv', 'Estabelecimentos8.csv',
            'Estabelecimentos9.csv'
]

## Definir tamanho do chunk
chunk_size = 1000

#################################################################################################

## Ler o arquivo com pandas
data = pd.read_csv('Estabelecimentos0.csv', encoding='iso-8859-1', low_memory=False, nrows=10000)
cabecalho = data.columns.tolist()
valores_coluna = data['SITUACAO CADASTRAL']
print(valores_coluna)

########################################################################################################

# Iterar sobre os chunks do arquivo CSV
for chunk in pd.read_csv('Socios5.csv', encoding='iso-8859-1', low_memory=False, chunksize=chunk_size, nrows=10000):
    # Obter valores da coluna "SITUACAO CADASTRAL"
    valores_coluna = chunk['NOME DO SOCIO (NO CASO PF) OU RAZAO SOCIAL (NO CASO PJ)']

    # Imprimir os valores da coluna
    print(valores_coluna)

########################################################################################################

##Nome coluna
nome_coluna = 'CNPJ BASICO'


## Criar uma lista para armazenar os valores da coluna
valores_coluna = []

## Percorrer a lista de arquivos CSV
for estabelCSV in estabelCSV:
    # Ler o arquivo CSV em chunks
    for chunk in pd.read_csv(estabelCSV, encoding='iso-8859-1', low_memory=False, chunksize=chunk_size, nrows=1000):
        # Acessar a coluna desejada no chunk atual
        coluna = chunk[nome_coluna]

        # Adicionar os valores da coluna ao final da lista
        valores_coluna.extend(coluna)

# Imprimir os valores da coluna
print(valores_coluna)