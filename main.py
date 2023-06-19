import pandas as pd
import csv
import os


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
            'Estabelecimentos.3csv', 'Estabelecimentos.4csv' , 'Estabelecimentos5.csv',
            'Estabelecimentos.6csv', 'Estabelecimentos.7csv', 'Estabelecimentos8.csv',
            'Estabelecimentos.9csv'
]

# Definir tamanho do chunk
chunk_size = 1000

# Ler o arquivo com pandas
data = pd.read_csv('Estabelecimentos0.csv', encoding='iso-8859-1', low_memory=False, nrows=10000)
cabecalho = data.columns.tolist()
valores_coluna = data['SITUACAO CADASTRAL']
print(valores_coluna)

# Iterar sobre os chunks do arquivo CSV
for chunk in pd.read_csv('Estabelecimentos0.csv', encoding='iso-8859-1', low_memory=False, chunksize=chunk_size):
    # Obter valores da coluna "SITUACAO CADASTRAL"
    valores_coluna = chunk['CNPJ BASICO']

    # Imprimir os valores da coluna
    print(valores_coluna)

