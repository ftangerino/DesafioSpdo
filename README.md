
# Desafio Técnico - Data Pipeline <h3>


### Objetivo: <h5>

Construir um data pipeline completo, desde a extração até o processamento e exibição dos dados da Receita Federal.


### Pontos a cumprir: <h5>

1. Escolha da linguagem de programação: Você pode utilizar a linguagem de sua escolha para implementar o data pipeline. (Python, Node, Ruby) 
Se optar por Ruby, receberá pontuação extra.

2. Leitura dos dados: Utilize uma biblioteca ou módulo adequado para ler os arquivos CSV fornecidos. Se possível, leia todos os arquivos ESTABELECIMENTO disponíveis. O layout dos dados está incluso no link.
https://dadosabertos.rfb.gov.br/CNPJ/

3. Organização dos dados: Armazene os dados extraídos em uma estrutura de hash/dicionário, facilitando o acesso e manipulação posterior.

4. Banco de dados: Salve os dados no MongoDB localmente ou utilize o serviço gratuito MongoAtlas para armazená-los em um banco de dados na nuvem. Opte pela solução mais simples para esta etapa.

5. Leitura e processamento dos dados: Recupere os dados do banco de dados e realize as seguintes tarefas:

a. Calcule a porcentagem de empresas ativas (SITUAÇÃO CADASTRAL).

b. Conte a quantidade de empresas do setor de restaurantes abertas em cada ano, considerando o prefixo do CNAE PRINCIPAL e a DATA DE INÍCIO ATIVIDADE. O prefixo para empresas de restaurantes é 56.1xxxxx, por exemplo, 5611-2/03 representa um restaurante.

c. Determine a quantidade de empresas localizadas em um raio de 5 km do CEP 01422000. 

d. Crie uma tabela de correlação entre o CNAE FISCAL PRINCIPAL e o CNAE FISCAL SECUNDÁRIA


### Resolução: <h5>

https://drive.google.com/drive/folders/1DVnq9Gb2aLiJlzl7ZR3O683h4To--L31?usp=sharing


### Tecnologias utilizadas: <h4>

    * Python
    * Pandas (PyMongo)
    * MongoDB
    * OS


### Autor: <h7>

Francisco Eduardo Barros Tangerino