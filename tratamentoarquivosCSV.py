import pandas as pd
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
            'Estabelecimentos3.csv', 'Estabelecimentos4.csv' , 'Estabelecimentos5.csv',
            'Estabelecimentos6.csv', 'Estabelecimentos7.csv', 'Estabelecimentos8.csv',
            'Estabelecimentos9.csv'
]



##tratar os arquivos

chunk_size = 1000000

temp_file = 'temp9.csv'
file_path = 'Estabelecimentos9.CSV'


chunks = []


with open(temp_file, 'w') as f:
    f.write(','.join(estabelColunas) + '\n')

try:
    # Lê o arquivo CSV original em chunks, excluindo o cabeçalho existente
    for chunk in pd.read_csv(file_path, chunksize=chunk_size, sep=';', skiprows=1, encoding='iso-8859-1',header=None):
        # Concatena o chunk com o arquivo temporário
        chunk.to_csv(temp_file, mode='a', header=False, index=False)

    # Renomeia o arquivo temporário para substituir o arquivo original
    os.rename(file_path, temp_file)

    # Lê o arquivo CSV atualizado
    df = pd.read_csv(file_path)
    print(df.head())
except pd.errors.ParserError:
    pass