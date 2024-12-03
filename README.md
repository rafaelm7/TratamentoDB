# Conversor CSV para SQLite - Dados de Comércio Exterior

Este projeto consiste em um script Python que converte dados de comércio exterior do formato CSV para um banco de dados SQLite, facilitando consultas e análises posteriores.

## 📋 Pré-requisitos

- Python 3.6 ou superior
- Bibliotecas Python listadas em `requirements.txt`

## 🚀 Instalação

1. Clone o repositório: 
bash
git clone https://github.com/seu-usuario/csv-to-sqlite.git
cd csv-to-sqlite

2. Instale as dependências:
bash
pip install -r requirements.txt


## Estrutura do Arquivo CSV
O script espera um arquivo CSV com as seguintes colunas:
- Fluxo
- Ano
- Países
- UF do Produto
- URF
- Código Seção
- Descrição Seção
- Via
- Código SH6
- Descrição SH6
- Valor US$ FOB

## Uso
1. Coloque seu arquivo CSV no mesmo diretório do script
2. Execute o script:

bash
python csv_to_sqlite.py

O script irá:
- Criar um arquivo de banco de dados SQLite chamado `comercio_exterior.db`
- Converter os dados do CSV para uma tabela SQLite
- Criar índices para otimização de consultas
- Gerar logs do processo

## Estrutura do Banco de Dados
### Tabela: comercio_exterior
- Todos os campos do CSV são preservados
- Tipos de dados são otimizados para cada coluna
- Índices criados para:
  - Ano
  - Países
  - UF do Produto
  - Código SH6

## Logs
O script gera logs detalhados que incluem:
- Início do processo de leitura do CSV
- Processo de limpeza dos dados
- Criação do banco de dados
- Criação de índices
- Erros (se houverem)

## Tratamento de Erros
O script inclui tratamento de erros para:
- Problemas na leitura do arquivo CSV
- Erros de conversão de dados
- Falhas na criação do banco de dados
- Problemas na criação de índices

## Contribuindo
Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter um Pull Request.

## Suporte
Para suporte, por favor abra uma issue no repositório do GitHub.
